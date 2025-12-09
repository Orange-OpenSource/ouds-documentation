### Structure & Labels
- [ ] **Accessible context**: Provide descriptive text via `aria-label` or visually hidden text (e.g., "5 unread messages" not just "5") ([Orange labeling guidelines](https://a11y-guidelines.orange.com/en/web/develop/textual-content/))
- [ ] **Non-interactive element**: Badge should not receive keyboard focus as it is purely informational (WCAG 2.4.3)
- [ ] **Semantic association**: Position badge adjacent to its related element so context is clear to all users

### Visual Design
- [ ] **Text contrast**: Minimum 4.5:1 contrast ratio between count and background color ([Orange contrast guidelines](https://a11y-guidelines.orange.com/en/web/design/colors-and-contrasts/))
- [ ] **Color independence**: Don't rely solely on color to convey status; combine with text labels or icons when critical
- [ ] **Minimum size**: Ensure count text meets minimum 12px font size for readability

### Content
- [ ] **Meaningful counts**: ❌ "5" / ✅ "5 notifications" (via accessible label) ([Orange content guidelines](https://a11y-guidelines.orange.com/en/web/develop/textual-content/))
- [ ] **Truncation clarity**: Use "99+" pattern for large numbers with accessible full count available