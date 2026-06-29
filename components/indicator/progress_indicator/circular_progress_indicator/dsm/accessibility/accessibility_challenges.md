A progress indicator conveys a changing, often non-textual state, so its meaning must be exposed to assistive technologies and remain clear when motion is reduced or the view is zoomed. The hardest part is announcing progress meaningfully without flooding screen readers, and distinguishing determinate from indeterminate behavior.

### Key Challenges
- Communicating a live, changing value to assistive technology without constant interruptions
- Conveying status (success, error…) without relying on color alone
- Indeterminate waits have no value to report, yet must still signal activity
- Motion-based feedback must survive reduced-motion preferences and zoom

### Critical Success Factors
1. Correct `progressbar` role with an accessible name (3.3.2, 4.1.2)
2. Determinate value exposed via `aria-valuenow`/`min`/`max`; omitted when indeterminate
3. Non-text and status meaning not conveyed by color alone (1.4.1, 1.4.11)
4. Polite live updates and respect for reduced motion (2.3.3, 4.1.3)