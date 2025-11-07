### Critical Success Factors
<<<<<<< HEAD
1. **Proper labeling and association** (WCAG 3.3.2, 1.3.1): Labels programmatically linked via `for`/`id`, helper text and errors associated using `aria-describedby`
2. **Live region announcements** (WCAG 4.1.3): Character counter and error messages use `aria-live="polite"` so screen readers announce changes without interrupting user typing
3. **Keyboard accessibility** (WCAG 2.1.1): All functionality—entering text, scrolling content, accessing helper links—operable via keyboard alone
4. **Clear focus indication** (WCAG 2.4.7): Focus ring maintains ≥3:1 contrast ratio against background at all times, including when content scrolls
=======
1. Provide programmatically associated labels, helper text, and error messages using `aria-describedby` (WCAG 3.3.2, 4.1.2)
2. Announce character count changes and limit violations via live regions without disrupting composition flow (WCAG 4.1.3)
3. Ensure all functionality operates via keyboard including multi-line navigation, scrolling, and error correction (WCAG 2.1.1)
4. Maintain ≥3:1 contrast for focus indicators, error borders, and disabled text states (WCAG 2.4.7, 1.4.11)
=======
Multi-line text areas present unique challenges because they combine complex interaction patterns (auto-resize, scrolling, character limits) with real-time feedback requirements. Users with visual, motor, or cognitive disabilities need clear communication about available space, remaining characters, validation errors, and scrolling state—all while maintaining keyboard operability and screen reader compatibility throughout dynamic height changes.