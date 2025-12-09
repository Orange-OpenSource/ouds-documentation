### Structure & Labels
- [ ] **Accessible name**: Provide `aria-label` or visible text that describes the badge status ([Orange labelling guide](https://a11y-guidelines.orange.com/en/web/develop/textual-content/))
- [ ] **Semantic meaning**: Use `role="status"` for badges that convey current state information
- [ ] **Programmatic association**: Associate badge with related element using `aria-describedby` when needed

### Visual Design
- [ ] **Color contrast**: Ensure ≥3:1 contrast ratio between badge and adjacent background ([Orange contrast guide](https://a11y-guidelines.orange.com/en/web/design/colors-and-contrasts/))
- [ ] **Non-color indicators**: Supplement color with text labels or patterns for status meaning
- [ ] **Minimum size**: Maintain minimum 8px dimension; consider 16px+ for critical status information

### Content
- [ ] **Descriptive labels**: ❌ "Red badge" / ✅ "Error status" ([Orange text alternatives](https://a11y-guidelines.orange.com/en/web/develop/textual-content/))
- [ ] **Concise text**: Keep badge labels brief but meaningful—use full words when space permits