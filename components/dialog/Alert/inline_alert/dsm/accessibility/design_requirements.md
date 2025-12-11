### Structure & Labels
- [ ] **ARIA role**: Use `role="alert"` for urgent messages, `role="status"` for non-urgent feedback ([Orange ARIA guidance](https://a11y-guidelines.orange.com/en/web/develop/textual-content/))
- [ ] **Icon alt text**: Provide accessible names for status icons or mark as decorative if text conveys meaning
- [ ] **Semantic HTML**: Use appropriate heading levels within alerts if titles are included

### Visual Design
- [ ] **Color contrast**: Ensure 4.5:1 minimum for text, 3:1 for icons and borders ([Color contrast](https://a11y-guidelines.orange.com/en/web/design/colors-and-contrasts/))
- [ ] **Multiple cues**: Combine color with icon and text to convey status—never rely on color alone
- [ ] **Focus indicator**: Provide visible focus state (≥3:1 contrast) if alert contains interactive elements

### Content
- [ ] **Clear messaging**: ❌ "Error" / ✅ "Your password must contain at least 8 characters" ([Writing accessible content](https://a11y-guidelines.orange.com/en/editorial-content/))
- [ ] **Concise text**: Keep alert messages brief and scannable; link to details if needed