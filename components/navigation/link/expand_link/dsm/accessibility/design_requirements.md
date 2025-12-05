### Structure & Labels
- [ ] **Semantic role**: Use `<button>` element with `aria-expanded` attribute ([Orange - Interactive elements](https://a11y-guidelines.orange.com/en/web/develop/interactive-components/))
- [ ] **Programmatic relationship**: Connect trigger to content via `aria-controls` referencing content ID
- [ ] **Accessible name**: Label clearly describes action or content, available to assistive technology

### Visual Design
- [ ] **Focus indicator**: Visible ring with ≥3:1 contrast against adjacent colors ([Orange - Focus visibility](https://a11y-guidelines.orange.com/en/web/design/focus-visibility/))
- [ ] **State indication**: Chevron direction change provides visual expanded/collapsed feedback
- [ ] **Disabled state**: Reduced opacity (0.2-0.28) indicates non-interactive state

### Content
- [ ] **Label clarity**: ❌ "Click here" / ✅ "Show payment options" ([Orange - Link labeling](https://a11y-guidelines.orange.com/en/web/design/navigation/))
- [ ] **State announcement**: Screen readers announce "expanded" or "collapsed" with label