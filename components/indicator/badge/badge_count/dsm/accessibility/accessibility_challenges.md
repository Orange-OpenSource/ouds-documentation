Badge counts present unique accessibility challenges because they convey dynamic numerical information through small visual indicators that must be perceivable by all users regardless of ability. The compact size, reliance on color for status meaning, and non-interactive nature require careful implementation to ensure screen reader users receive equivalent information.

### Key Challenges

- Small size makes meeting 4.5:1 contrast ratio critical for text legibility
- Status colors must not be the sole method of conveying semantic meaning
- Dynamic count updates need to be announced to assistive technology users
- Non-interactive nature means badges should not receive keyboard focus

### Critical Success Factors

1. Maintain 4.5:1 minimum contrast ratio between count text and background (WCAG 1.4.3)
2. Provide programmatic text alternatives via `aria-label` or visually hidden text
3. Use `aria-live` regions for dynamic count updates when contextually important
4. Ensure status meaning is conveyed through context, not color alone