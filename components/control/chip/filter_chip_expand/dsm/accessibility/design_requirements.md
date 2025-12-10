### Structure & Labels

- [ ] **Accessible name**: Provide descriptive label via visible text or `aria-label` ([Orange label guidelines](https://a11y-guidelines.orange.com/en/web/develop/textual-content/))
- [ ] **Role announcement**: Use `role="combobox"` with `aria-haspopup="listbox"` for proper semantics
- [ ] **State communication**: Set `aria-expanded` to "true" or "false" reflecting dropdown visibility

### Visual Design

- [ ] **Focus indicator**: Triple-border focus ring with ≥3:1 contrast against background ([Focus guidelines](https://a11y-guidelines.orange.com/en/web/design/colors-and-contrasts/))
- [ ] **State distinction**: Selected vs unselected states distinguishable without relying on color alone
- [ ] **Touch target**: Minimum 48×48px interactive area for mobile accessibility

### Content

- [ ] **Label clarity**: ❌ "Filter 1" / ✅ "Size" or "Price range" ([Content guidelines](https://a11y-guidelines.orange.com/en/web/develop/textual-content/))
- [ ] **Counter announcement**: Badge count included in accessible name (e.g., "Size, 3 selected")