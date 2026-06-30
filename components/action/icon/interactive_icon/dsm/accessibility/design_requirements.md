### Structure & Labels

- [ ] **Semantic markup**: Wrap the icon in a native `<button>` for automatic keyboard and screen-reader support
- [ ] **Accessible name**: Always provide a descriptive `aria-label` ([Label guidance](https://a11y-guidelines.orange.com/en/web/develop/textual-content/#make-sure-the-user-can-use-native-browser-options))
- [ ] **State communication**: Expose the Loading state with `aria-busy="true"` and announce completion

### Visual Design

- [ ] **Focus visibility**: Display a focus ring with ≥3:1 contrast against adjacent colors ([Focus guidance](https://a11y-guidelines.orange.com/en/web/design/navigation-focus/))
- [ ] **Color independence**: State is shown by color only — pair it with focus and the icon so meaning isn't color-dependent
- [ ] **Interactive area**: Maintain at least a 28px interactive target; enlarge it for touch-first contexts

### Content

- [ ] **Descriptive name**: ❌ "icon" / ✅ "Close dialog" ([Content guidance](https://a11y-guidelines.orange.com/en/web/design/textual-content/))
- [ ] **No duplication**: If a visible label already exists nearby, don't repeat it redundantly in the accessible name