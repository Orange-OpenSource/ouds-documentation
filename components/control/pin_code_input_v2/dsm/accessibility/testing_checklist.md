### Testing Checklist

**Quick Tests (≤5 minutes)**

1. Complete digit entry using keyboard only: Tab through boxes, type digits, Backspace to correct, Enter to submit; verify visible focus indicators (≥2px, ≥3:1 contrast).
2. Screen reader announces group label ("Enter 6-digit verification code"), individual box labels ("Digit 1 of 6"), and error messages immediately upon submission failure.
3. Zoom to 200%: digit boxes reflow without horizontal scrolling; all text and controls remain readable and functional.
4. High-contrast mode: focus indicators, error borders, and state cues remain perceivable with ≥3:1 contrast.
5. Touch device: numeric keyboard opens on focus; each box meets 44×44px; layout adapts to portrait/landscape without breaking.

**Common Issues to Avoid**

1. Missing `aria-labelledby` on the group or `aria-label` on individual digit boxes.
2. Error state indicated by color change only without accompanying text message or `aria-invalid`.
3. Focus indicator contrast <3:1 or outline <2px width.
4. Auto-advance not announced by screen readers or causing focus to skip boxes.
5. Missing `inputmode="numeric"` on mobile, forcing users to switch keyboard layouts manually.