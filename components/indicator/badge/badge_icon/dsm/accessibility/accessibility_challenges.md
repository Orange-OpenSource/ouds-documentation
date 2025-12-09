Icon-only badges present unique accessibility challenges because they rely heavily on visual cues—color and iconography—to communicate status. Users with color vision deficiencies, cognitive impairments, or those using assistive technologies may not perceive the intended meaning without proper implementation.

### Key Challenges

- Color alone cannot convey status meaning—icons must be recognizable and labeled
- Small badge sizes make icons difficult to perceive for users with low vision
- Non-interactive badges must still communicate their purpose to screen readers
- Functional icons must maintain semantic consistency across all status types

### Critical Success Factors

1. Ensure 4.5:1 minimum contrast ratio between icon and background (WCAG 1.4.3)
2. Provide accessible names via `aria-label` when badges lack visible text
3. Use `aria-hidden="true"` when context is provided by surrounding elements
4. Pair icons with visible text labels whenever space permits