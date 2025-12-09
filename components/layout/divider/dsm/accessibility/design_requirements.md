### Structure & Labels
- [ ] **Semantic HTML**: Use `<hr>` for thematic breaks; use `<div role="separator">` for menu dividers
- [ ] **Decorative hiding**: Apply `aria-hidden="true"` to purely visual dividers ([Orange A11y - Hide elements](https://a11y-guidelines.orange.com/en/web/components-examples/))
- [ ] **Orientation attribute**: Set `aria-orientation="vertical"` for vertical dividers

### Visual Design
- [ ] **Sufficient contrast**: Ensure divider has ≥3:1 contrast ratio against adjacent backgrounds ([Orange A11y - Colors](https://a11y-guidelines.orange.com/en/web/design/colors-and-contrasts/))
- [ ] **Consistent styling**: Use design tokens for divider colors to maintain visual consistency
- [ ] **Adequate spacing**: Provide sufficient margin around dividers for visual clarity

### Content
- [ ] **No semantic children**: ❌ `<hr><h2>Title</h2></hr>` / ✅ Place headings outside dividers
- [ ] **Meaningful breaks only**: Use semantic dividers only for actual thematic breaks between content