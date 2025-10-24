### Testing Checklist

**Quick Tests (≤5 minutes)**

1. Complete digit entry using keyboard only with visible focus moving sequentially; `Backspace` navigates backward correctly.
2. Screen reader announces each field position ("Digit 1 of 6"), group label, and error messages immediately upon validation failure.
3. Zoom to 200%: all input fields remain visible and functional without horizontal scrolling; layout reflows appropriately.
4. High-contrast mode: focus indicators, field borders, and error states remain clearly visible with ≥3:1 contrast.
5. On touch device: numeric keyboard opens automatically; targets are ≥44×44px; auto-advance works between fields.

**Common Issues to Avoid**

1. Missing group label or individual field position announcements for screen reader users.
2. Color-only error indication without accompanying error icon or descriptive error message text.
3. Missing `aria-invalid="true"` or `aria-describedby` linking error message to input fields in error state.
4. Insufficient contrast (<3:1) for focus indicators or error state borders against background.
5. Focus trap within digit fields preventing users from navigating to submit button or other page elements.
6. Auto-advance not working or moving focus before users can correct a mistyped digit.