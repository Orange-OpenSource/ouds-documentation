Badge counts present unique accessibility challenges because they are non-interactive visual indicators that communicate dynamic numeric information. Users must be able to perceive badge updates through multiple channels, and screen reader users need equivalent access to count changes without requiring focus navigation to the badge element.

### Key Challenges
- Color-only status differentiation may exclude users with color vision deficiencies
- Dynamic count updates may not be announced to screen reader users
- Small text size within badges can impact readability for users with low vision
- Non-interactive nature means standard focus-based announcement patterns don't apply

### Critical Success Factors
1. Maintain 4.5:1 minimum contrast ratio between count text and background (WCAG 1.4.3)
2. Provide programmatic context through `aria-label` or adjacent text for screen readers
3. Use ARIA live regions to announce count changes when updates occur dynamically
4. Ensure status meaning is conveyed through more than color alone