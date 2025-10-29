## Testing Checklist

**Quick Tests (≤5 minutes)**

1. Navigate the component using only the keyboard (`Tab`, `Shift+Tab`, arrow keys) with visible focus indicators at all times.
2. Use a screen reader to verify labels, helper text, and error messages are announced correctly and immediately.
3. Zoom the page to 200% and confirm the layout reflows without content loss, overlap, or horizontal scrolling.
4. Enable high-contrast mode or dark mode and verify focus indicators, borders, and text remain perceivable.
5. On a touch device, confirm buttons meet 44×44px minimum size and the numeric keyboard appears when tapping the input.

**Common Issues to Avoid**

1. Using color alone to indicate error state without accompanying text, icons, or border changes.
2. Missing `aria-invalid` and `aria-describedby` attributes on inputs with validation errors.
3. Focus indicators with insufficient contrast (<3:1) or missing entirely.
4. Buttons or interactive elements smaller than 44×44px on mobile devices.
5. Error messages not linked to inputs programmatically, causing screen readers to miss announcements.