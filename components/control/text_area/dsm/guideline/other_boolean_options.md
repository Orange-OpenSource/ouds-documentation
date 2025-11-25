**Scrolled** Represents the state in which the field contains more text than its visible height can display and that internal scrolling is available. This allows users to navigate through the overflowing text without expanding the text area beyond **the maximum planned height of 240px, allowing the display of about 10 lines of text**. It is particularly useful when preserving space is important, or when the text area is embedded within a fixed-height container.

**Helper text** Supporting text conveys additional information about the input field, such as how it will be used. It should ideally only take up a single line, though may wrap to multiple lines if required, and be either persistently visible or visible only on focus.

**Helper link** If the helper text is not sufficient (It can also be displayed on its own without helper text), it's possible to offer the user an additional help link (the link can be external or open a modal).

**Do & don'ts**

✅ **Do:** Set a maximum height for text areas to prevent them from dominating the layout, using scrolling for overflow content

❌ **Don't:** Allow text areas to expand infinitely without constraint, as this disrupts page layout and creates poor mobile experiences

✅ **Do:** Use helper text to provide concise, actionable guidance that helps users understand what to enter

❌ **Don't:** Make helper text longer than 1-2 lines, as lengthy instructions reduce scannability and increase cognitive burden

✅ **Do:** Position helper text directly below the text area where users naturally look for additional context

❌ **Don't:** Place helper text above the text area or far from it, as this breaks the visual flow and reduces discoverability

✅ **Do:** Use helper links sparingly for detailed instructions that would overwhelm inline helper text

❌ **Don't:** Include links within helper text without clear indication, as screen readers may not announce them as interactive

✅ **Do:** Ensure scrolled text areas have sufficient contrast on scrollbars and clear visual indicators of scrollable content

❌ **Don't:** Hide scrollbars entirely, as users need visual confirmation that more content exists below

✅ **Do:** Test scrolling behavior on mobile devices to avoid nested scrolling issues where possible

❌ **Don't:** Create scroll-within-scroll situations on mobile, as they cause frustration and usability problems

✅ **Do:** Make helper text and helper links accessible via screen readers using proper semantic markup

❌ **Don't:** Convey critical information only through helper links, as users may miss or skip them

✅ **Do:** Display helper text persistently rather than only on focus, ensuring it's available when users need it most

❌ **Don't:** Rely on hover-only tooltips for essential information, as they're not accessible on touch devices or to keyboard users