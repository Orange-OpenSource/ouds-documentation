Select inputs present unique accessibility challenges due to their dual nature as both form controls and interactive menus. The native HTML `<select>` element provides built-in accessibility, but custom-styled implementations often break keyboard navigation, screen reader compatibility, and focus management. Users with motor impairments struggle with precise mouse control required for dropdown interactions, while screen reader users may not receive adequate feedback about available options, current selections, or state changes.

### Key Challenges
- Custom-styled selects often break native keyboard navigation and screen reader support
- Dropdown menus disappearing before users can make selections with assistive technology
- Insufficient feedback when options are filtered, loaded asynchronously, or change dynamically
- Lack of proper ARIA attributes causing screen readers to misidentify component type and state

### Critical Success Factors
1. Maintain full keyboard operability (`Tab`, `Enter`, `Space`, `Arrow keys`, `Escape`) with clear focus indicators meeting 3:1 contrast ratio
2. Implement proper ARIA semantics (`role="combobox"`, `aria-expanded`, `aria-owns`, `aria-activedescendant`) to communicate component structure
3. Associate labels, error messages, and helper text programmatically using `aria-labelledby` and `aria-describedby`
4. Announce all state changes and dynamic content updates to screen readers in real-time