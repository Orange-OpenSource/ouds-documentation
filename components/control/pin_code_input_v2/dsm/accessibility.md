# Accessibility

### Keyboard Support

1. **`Tab`** moves focus forward through each digit box in left-to-right order; **`Shift+Tab`** moves focus backward.
2. Typing a valid digit (0–9) automatically advances focus to the next empty box; typing in the last box keeps focus on that box.
3. **`Backspace`** deletes the current digit and moves focus to the previous box; pressing Backspace in an empty box moves to the previous box without deleting.
4. **`Enter`** submits the form when all required digits are filled; focus remains on the last box if submission fails.
5. Provide a visible focus indicator with outline/border ≥2px and contrast ≥3:1 around the active digit box.
6. Arrow keys (**`ArrowLeft`**, **`ArrowRight`**) may optionally navigate between boxes; document this behavior if implemented.

---

### Screen Reader Experience

1. Use `<input type="text" inputmode="numeric" maxlength="1">` for each digit box to enforce single-character numeric entry.
2. Label the entire group using `role="group"` with `aria-labelledby` pointing to a heading (e.g., "Enter 6-digit verification code").
3. Each digit box must have a programmatic label such as `aria-label="Digit 1 of 6"` to indicate position in the sequence.
4. Apply `aria-invalid="true"` to all digit boxes when the error state is active; link error text using `aria-describedby` with a stable ID.
5. Announce error messages immediately upon submission failure using `aria-live="assertive"`; announce success states with `aria-live="polite"`.
6. When focus auto-advances, screen readers announce the new box label (e.g., "Digit 2 of 6") without additional interruption.

---

### Touch & Mobile

1. Provide touch targets ≥44×44px (48×48 preferred) for each digit box with spacing ≥8px between boxes.
2. Trigger numeric keyboard automatically using `inputmode="numeric"` to streamline digit entry on mobile devices.
3. Support both portrait and landscape orientations; boxes must reflow or scale responsively without loss of functionality.
4. Ensure visible focus indicators remain perceivable on touch devices (outline ≥2px, contrast ≥3:1) when using external keyboards.

---

### Visual Accessibility

1. Ensure digit box borders, focus indicators, and error outlines have contrast ≥3:1 against adjacent colors.
2. Error state must include both color change (e.g., red border) and a text message below the component; do not rely on color alone.
3. Helper text and error messages must have text contrast ≥4.5:1; large text (≥18pt or ≥14pt bold) requires ≥3:1.
4. Support text resizing up to 200%; boxes and text must reflow without horizontal scrolling or content loss (WCAG 2.1 Reflow).
5. Respect `prefers-reduced-motion` for focus transitions and auto-advance animations; reduce or eliminate motion when requested.

---

### Error Handling

1. Apply `aria-invalid="true"` to all digit boxes when the error state is active (submission with incomplete or incorrect entry).
2. Link error text to the group using `aria-describedby` with a stable ID (e.g., `id="pin-error"`); ensure each box references this ID.
3. Announce error messages immediately upon submission using `aria-live="assertive"`; message content must match displayed text.
4. Provide specific error messages: "Please enter the verification code." (empty case) or "Verification failed. Check and enter the correct code." (incorrect case).
5. Upon successful resubmission, remove `aria-invalid` and announce success with `aria-live="polite"` (e.g., "Code accepted"); return focus to the next logical element or first digit box for retry.

---

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