### Structure & Labels

- [ ] **Semantic markup**: Use `<span>` with appropriate `role` or descriptive context for status tags
- [ ] **Text alternatives**: Provide `aria-label` for icon-only tags or hidden text for screen readers
- [ ] **Meaningful labels**: Keep tag text concise (1-3 words) while remaining descriptive ([Writing accessible content](https://a11y-guidelines.orange.com/en/editorial-content/))

### Visual Design

- [ ] **Color contrast**: Minimum 4.5:1 ratio for text on both muted and emphasized backgrounds ([Color contrast](https://a11y-guidelines.orange.com/en/web/design/colors-and-contrasts/))
- [ ] **Don't rely on color alone**: Pair status colors with text labels and/or icons
- [ ] **Focus indicator**: Not required for non-interactive tags; ensure adjacent interactive elements have visible focus

### Content

- [ ] **Clear status text**: ❌ "New" alone / ✅ "New feature" or provide context via surrounding content
- [ ] **Icon meaning**: Functional icons must match their semantic purpose (success, warning, error, info)