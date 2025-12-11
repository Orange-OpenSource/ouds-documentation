### Structure & Labels

- [ ] **Accessible name**: Provide descriptive `aria-label` (e.g., "5 unread notifications") conveying count purpose ([Orange A11y - Accessible Name](https://a11y-guidelines.orange.com/en/web/develop/textual-content/))
- [ ] **Hidden text alternative**: Include visually hidden text for screen readers when badge is purely visual
- [ ] **Contextual association**: Ensure badge is programmatically associated with its parent element via proximity or `aria-describedby`

### Visual Design

- [ ] **Color contrast**: Minimum 4.5:1 ratio between count text and background color ([Orange A11y - Colors](https://a11y-guidelines.orange.com/en/web/design/colors-and-contrasts/))
- [ ] **Non-color identification**: Status meaning conveyed through context/labels, not color alone
- [ ] **Minimum size**: Ensure count text meets minimum target size for legibility

### Content

- [ ] **Meaningful counts**: ❌ "99+" without context / ✅ "99+ unread messages" with full context available
- [ ] **Truncation handling**: Provide full count value to assistive technology when visually truncated