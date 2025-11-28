### Structure & Labels
- [ ] **Every select input must have a visible or programmatically associated label**: Use `<label>` element with `for` attribute or `aria-labelledby` ([Orange: Form labels](https://a11y-guidelines.orange.com/en/web/components-examples/forms/))
- [ ] **Required fields must be indicated accessibly**: Use `aria-required="true"` and visual indicator with legend explaining convention
- [ ] **Associate helper text and error messages**: Use `aria-describedby` to link supplementary text to the input element

### Visual Design
- [ ] **Focus indicator must have ≥3:1 contrast ratio**: Ensure keyboard focus is clearly visible against background ([Orange: Focus visible](https://a11y-guidelines.orange.com/en/web/components-examples/accessible-components/focus-visible/))
- [ ] **Error states must not rely on color alone**: Include icon and descriptive text alongside color change ([WCAG 1.4.1](https://a11y-guidelines.orange.com/en/web/design/colors-and-contrasts/))
- [ ] **Text and icons meet contrast requirements**: Minimum 4.5:1 for text, 3:1 for icons and borders

### Content
- [ ] **Option text must be clear and concise**: ❌ "Option 1" / ✅ "Credit card payment" ([Orange: Clear content](https://a11y-guidelines.orange.com/en/articles/user-tests-accessibility/))
- [ ] **Error messages must be specific and actionable**: Describe the problem and how to fix it (e.g., "Please select a delivery method")