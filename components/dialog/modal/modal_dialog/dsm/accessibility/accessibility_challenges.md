A modal dialog interrupts the page and takes over interaction. Users of assistive technologies must be told that a dialog has opened, must be kept inside it while it is open, and must be returned to where they were when it closes.

### Key Challenges

- Focus must move into the dialog when it opens and stay inside it until it closes
- The page behind the backdrop must be unavailable to keyboard and screen reader users, not only visually dimmed
- Visual action order on tablet and desktop can differ from the logical order Primary → Secondary → Tertiary
- Long content, sticky actions and zoom must not hide the title, the actions or the focused element

### Critical Success Factors

1. Expose the dialog with `role="dialog"` and `aria-modal="true"`, named by its always-visible title through `aria-labelledby`, and make the page behind inert (WCAG 4.1.2)
2. Move focus into the dialog on opening, keep Tab and Shift+Tab cycling inside it, and return focus to the triggering element on closing (WCAG 2.4.3)
3. Always provide a keyboard-operable way to dismiss the dialog, including the Escape key, unless the flow intentionally prevents dismissal
4. Keep the DOM and focus order of actions Primary → Secondary → Tertiary whatever their visual position