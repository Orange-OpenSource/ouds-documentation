### Structure & Labels

- [ ] **Container role**: Use `role="group"` or `role="listbox"` with `aria-label` describing the input purpose
- [ ] **Tag identification**: Each tag uses `role="option"` with accessible name from label text
- [ ] **Remove button**: Close icon has `aria-label="Remove [tag name]"` ([Orange ARIA guidelines](https://a11y-guidelines.orange.com/en/web/develop/textual-content/))

### Visual Design

- [ ] **Focus indicator**: 3:1 minimum contrast ratio with ≥2px visible border ([Focus visibility](https://a11y-guidelines.orange.com/en/web/design/focus-visibility/))
- [ ] **State differentiation**: Enabled, hover, pressed, disabled states visually distinct with sufficient contrast
- [ ] **Text contrast**: Label text meets 4.5:1 contrast ratio against background

### Content

- [ ] **Concise labels**: ❌ "Click here to remove this particular tag item" / ✅ "Remove Marketing" ([Clear labels](https://a11y-guidelines.orange.com/en/web/design/content/))
- [ ] **Consistent terminology**: Use same remove action label pattern across all tags