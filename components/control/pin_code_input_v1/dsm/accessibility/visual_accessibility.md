### Visual Accessibility

1. Ensure text contrast **≥4.5:1** for digit characters and helper/error text; large text (helper) requires **≥3:1**.
2. Ensure focus indicators and digit box borders have contrast **≥3:1** against the background.
3. Use both color and text to convey error state; apply red border + "Verification failed" message (do not rely on color alone).
4. Support text resizing up to **200%** without loss of content or functionality; digit boxes must reflow without horizontal scroll.
5. Respect `prefers-reduced-motion`; avoid animated transitions for focus movement or error appearance.