### Structure & Labels

- [ ] **Semantic markup**: Use the native `<button>` element for automatic keyboard and screen-reader support
- [ ] **Accessible name**: Provide a descriptive label or `aria-label` for "Icon only" buttons ([Label guidance](https://a11y-guidelines.orange.com/en/web/develop/textual-content/#make-sure-the-user-can-use-native-browser-options))
- [ ] **State communication**: Expose the Loading state with `aria-busy="true"` and announce completion

### Visual Design

- [ ] **Focus visibility**: Display a focus ring with ≥3:1 contrast against adjacent colors ([Focus guidance](https://a11y-guidelines.orange.com/en/web/design/navigation-focus/))
- [ ] **Color independence**: Don't rely on color alone to signal state; keep the icon and focus cues
- [ ] **Touch targets**: Maintain a minimum 48×48px interactive area at every size

### Content

- [ ] **Descriptive labels**: ❌ "Go" / ✅ "Ask the AI assistant" ([Content guidance](https://a11y-guidelines.orange.com/en/web/design/textual-content/))
- [ ] **Decorative icon**: Mark the sparkle icon as decorative when a visible label already conveys the action