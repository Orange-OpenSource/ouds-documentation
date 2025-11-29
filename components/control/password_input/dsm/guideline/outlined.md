**`False`** An input with a subtle background fill and un visible bottom border, creating a softer and more contained look. Best suited for dense layouts or to enhance visibility.

**`True`** A minimalist input with a transparent background and a visible stroke outlining the field. This style may be interesting for contexts other than form pages:
• When inputs need to feel lightweight and unobtrusive
• In a header (search field)
• In a selection/filtering feature in a product catalog

### Do & don'ts

✅ **Do:** Use the outlined style in lightweight contexts such as headers, filters, or search interfaces where minimal visual weight improves the experience.  
❌ **Don't:** Mix outlined and filled styles inconsistently within the same form—choose one style and apply it uniformly.

✅ **Do:** Select the filled (non-outlined) variant for standard form pages to ensure sufficient visual prominence and discoverability.  
❌ **Don't:** Use the outlined style in dense forms where users need strong visual boundaries to distinguish multiple adjacent fields.

✅ **Do:** Ensure both outlined and filled variants maintain the same functional behaviors including focus states and error handling.  
❌ **Don't:** Reduce the touch target size when using the outlined style—maintain minimum 44×44px interactive areas.

✅ **Do:** Test both style variants for adequate contrast against their background contexts in light and dark modes.  
❌ **Don't:** Assume the outlined style will work on busy backgrounds without verifying stroke visibility meets 3:1 contrast ratio.

✅ **Do:** Apply the outlined style when aligning with brand guidelines that favor a modern, minimal aesthetic.  
❌ **Don't:** Choose style variants based solely on personal preference—align with established design system patterns.