### Structure & Labels

- [ ] **Semantic button element**: Use `<button>` with `aria-pressed` attribute ([Orange guidelines](https://a11y-guidelines.orange.com/en/web/develop/custom-components/))
- [ ] **Accessible name**: Provide visible label text or `aria-label` for icon-only variants
- [ ] **Group labeling**: Wrap chip groups with `role="group"` and `aria-label` describing the filter category

### Visual Design

- [ ] **Color contrast**: Maintain 4.5:1 contrast for text, 3:1 for graphical elements ([Color contrast](https://a11y-guidelines.orange.com/en/web/design/colors-and-contrasts/))
- [ ] **Focus visibility**: Display triple-border focus ring with 3:1 contrast against adjacent colors
- [ ] **Touch target**: Ensure minimum 48×48px interactive area for all chip variants

### Content

- [ ] **Label clarity**: ❌ "Filter: Category" / ✅ "Category" ([Writing guidelines](https://a11y-guidelines.orange.com/en/web/design/textual-content/))
- [ ] **State announcement**: Ensure selected state is conveyed through both visual and programmatic means