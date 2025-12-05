Switches present unique accessibility challenges because they communicate binary state changes that must be perceivable, operable, and understandable across all input methods and assistive technologies. The visual metaphor of a physical switch doesn't translate directly to non-visual contexts.

### Key Challenges
- Communicating current state (on/off) clearly to screen reader users without visual cues
- Ensuring immediate state changes are announced without disrupting user workflow
- Maintaining consistency between visual appearance and programmatic state
- Supporting both touch and keyboard interaction with adequate target sizes

### Critical Success Factors
1. Use `role="switch"` with `aria-checked` to properly convey on/off semantics (WCAG 4.1.2)
2. Provide visible focus indicators meeting 3:1 contrast ratio (WCAG 2.4.7)
3. Ensure label text clearly describes what the switch controls (WCAG 3.3.2)
4. Associate error messages programmatically using `aria-describedby` (WCAG 3.3.1)