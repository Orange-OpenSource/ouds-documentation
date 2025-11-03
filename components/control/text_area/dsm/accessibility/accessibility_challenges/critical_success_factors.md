### Critical Success Factors
1. **Proper labeling and association** (WCAG 3.3.2, 1.3.1): Labels programmatically linked via `for`/`id`, helper text and errors associated using `aria-describedby`
2. **Live region announcements** (WCAG 4.1.3): Character counter and error messages use `aria-live="polite"` so screen readers announce changes without interrupting user typing
3. **Keyboard accessibility** (WCAG 2.1.1): All functionality—entering text, scrolling content, accessing helper links—operable via keyboard alone
4. **Clear focus indication** (WCAG 2.4.7): Focus ring maintains ≥3:1 contrast ratio against background at all times, including when content scrolls