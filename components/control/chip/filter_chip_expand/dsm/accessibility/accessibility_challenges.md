The Expand Filter Chip presents unique accessibility challenges because it combines interactive button behavior with a dropdown popup. The component must communicate its dual nature (filter indicator and expandable control), announce state changes clearly, and maintain proper focus management when the dropdown opens and closes.

### Key Challenges

- Communicating the expandable nature and current selection status to screen readers
- Managing focus between the chip and the dropdown popup without disorienting users
- Ensuring the chevron icon direction change is perceivable by all users
- Providing keyboard access to all dropdown options while maintaining logical tab order

### Critical Success Factors

1. Use `role="combobox"` with proper `aria-expanded` and `aria-haspopup="listbox"` attributes
2. Announce selection count and expanded state changes via live regions or ARIA attributes
3. Implement complete keyboard navigation following WAI-ARIA combobox pattern
4. Maintain visible focus indicators with ≥3:1 contrast ratio throughout all interactions