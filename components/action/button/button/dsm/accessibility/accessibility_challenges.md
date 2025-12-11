Buttons present unique accessibility challenges due to their diverse appearances (Strong, Default, Minimal, Brand, Negative), multiple layouts (text-only, icon-only, text+icon), and various states that must all communicate clearly to assistive technologies.

### Key Challenges

- Icon-only buttons require explicit accessible labels since visual icons alone provide no information to screen readers
- Focus states must be clearly visible across all appearance variants and background contexts
- Loading and disabled states must communicate programmatically, not just visually
- Buttons on colored backgrounds require careful contrast management

### Critical Success Factors

1. Use semantic `<button>` element or `role="button"` with proper keyboard handling
2. Ensure all interactive states have ≥3:1 contrast for focus indicators and ≥4.5:1 for text
3. Provide `aria-label` for icon-only buttons and `aria-describedby` for additional context
4. Communicate loading/disabled states via `aria-busy` and `aria-disabled` attributes