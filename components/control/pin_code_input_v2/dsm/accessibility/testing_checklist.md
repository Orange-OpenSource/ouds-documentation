### Testing Checklist

**Quick Tests (≤5 minutes)**

1. Navigate through all digit fields using only `Tab`, number keys, and `Backspace`; verify focus indicators are visible at ≥3:1 contrast.
2. With a screen reader, confirm the group label, helper text, and error messages are announced correctly when navigating fields.
3. Zoom to 200%: all digit fields, helper text, and error messages remain visible and functional without horizontal scrolling.
4. Enable high-contrast mode: verify field borders, focus indicators, and error states remain clearly distinguishable.
5. On a mobile device, confirm the numeric keyboard opens automatically and touch targets meet 44×44px.

**Common Issues to Avoid**

1. Missing `aria-invalid` or `aria-describedby` on digit fields when error state is active.
2. Error state conveyed only by red color without accompanying error text or icon.
3. Focus indicators with insufficient contrast (<3:1) making keyboard navigation difficult to track.
4. Auto-advance behavior that doesn't work correctly with screen readers or keyboard-only users.