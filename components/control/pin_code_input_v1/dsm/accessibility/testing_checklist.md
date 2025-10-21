### Testing Checklist

**Quick Tests (≤5 minutes)**

1. Keyboard-only: `Tab` into first box, type digits with auto-advance, use `Backspace` to correct, and submit; verify visible focus indicator ≥2px with ≥3:1 contrast.
2. Screen reader announces "Enter 6-digit verification code" on focus; error message "Verification failed. Check and enter the correct code." reads immediately after failed submission.
3. Zoom to **200%**: digit boxes reflow without horizontal scroll; spacing and focus indicators remain perceivable.
4. High-contrast/dark mode: focus indicators and error state remain visible with ≥3:1 contrast; red border alone is not the only error cue.
5. On a touch device: paste 6-digit code from SMS via long-press; verify numeric keyboard opens and all boxes populate correctly.

**Common Issues to Avoid**

1. Missing `aria-invalid="true"` on digit boxes when error state is active.
2. Replacing helper text entirely with error message (both must remain visible simultaneously).
3. Focus indicators with insufficient contrast (<3:1) against the background.
4. Blocking paste or failing to distribute pasted digits across all boxes.
5. Individual digit validation errors instead of unified group-level error state.