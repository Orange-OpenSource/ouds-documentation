### Structure & Labels

- [ ] **Trigger semantics**: A `button` in a heading element; the label, overline, extra label and description form its accessible name and description ([Orange ARIA guidelines](https://a11y-guidelines.orange.com/en/web/develop/textual-content/))
- [ ] **State**: `aria-expanded` reflects the Expanded property; a Disabled item uses `aria-disabled` or the `disabled` attribute
- [ ] **Decorative visuals**: Decorative leading and trailing visuals are hidden from assistive technologies; informative ones have a text alternative

### Visual Design

- [ ] **Focus indicator**: 3:1 minimum contrast ratio with ≥2px visible border around the complete trigger ([Focus visibility](https://a11y-guidelines.orange.com/en/web/design/focus-visibility/))
- [ ] **Indicator contrast**: The Expanding indicator meets 3:1 against its background in every state
- [ ] **Target size**: The trigger is interactive across its full width and at least 24 × 24 CSS px

### Content

- [ ] **Descriptive labels**: ❌ "More" / ✅ "Delivery and returns" ([Clear labels](https://a11y-guidelines.orange.com/en/web/design/content/))
- [ ] **Concise triggers**: Supporting text stays short so the announced button text remains easy to follow