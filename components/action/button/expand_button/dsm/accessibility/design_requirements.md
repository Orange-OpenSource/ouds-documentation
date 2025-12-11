### Structure & Labels

- [ ] **Semantic markup**: Use native `<button>` element for automatic keyboard and screen reader support
- [ ] **Accessible name**: Provide descriptive text label or `aria-label` for icon-only variants ([Visible label guidance](https://a11y-guidelines.orange.com/en/web/develop/textual-content/#make-sure-the-user-can-use-native-browser-options))
- [ ] **State communication**: Include `aria-expanded="true|false"` that updates on interaction

### Visual Design

- [ ] **Focus visibility**: Display focus ring with ≥3:1 contrast against adjacent colors ([Focus guidance](https://a11y-guidelines.orange.com/en/web/design/navigation-focus/))
- [ ] **Color independence**: Ensure state changes are not communicated by color alone; use chevron rotation
- [ ] **Touch targets**: Maintain minimum 44×44px interactive area for touch devices

### Content

- [ ] **Descriptive labels**: ❌ "More" / ✅ "Show payment options" ([Content guidance](https://a11y-guidelines.orange.com/en/web/design/textual-content/))
- [ ] **Consistent patterns**: Use same interaction model for all expand buttons in the interface