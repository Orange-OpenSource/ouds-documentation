Expand buttons present unique accessibility challenges because they control hidden content and must communicate both their current state (expanded/collapsed) and their relationship to the content they reveal. Users relying on assistive technology need clear announcements of state changes and predictable keyboard interaction.

### Key Challenges

- Communicating expanded/collapsed state to screen readers dynamically
- Ensuring keyboard users can operate the toggle with standard keys (Enter/Space)
- Providing accessible names for icon-only variants without visible labels
- Maintaining focus management when content expands or collapses

### Critical Success Factors

1. Use `aria-expanded` attribute that updates dynamically with state changes
2. Associate button with controlled content via `aria-controls` referencing content `id`
3. Provide visible focus indicator with ≥3:1 contrast ratio
4. Ensure icon-only buttons have accessible names via `aria-label`