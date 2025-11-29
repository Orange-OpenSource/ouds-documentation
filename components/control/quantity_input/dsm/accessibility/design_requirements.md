### Structure & Labels
- [ ] **Programmatic label**: Associate visible label with input using `<label for="">` or `aria-labelledby` ([Orange labelling guidelines](https://a11y-guidelines.orange.com/en/web/develop/textual-content/#labelling-form-elements))
- [ ] **Spinbutton role**: Apply `role="spinbutton"` with `aria-valuenow`, `aria-valuemin`, `aria-valuemax` attributes
- [ ] **Button labels**: Provide accessible names for increment/decrement buttons ("Increase quantity", "Decrease quantity")

### Visual Design
- [ ] **Focus indicator**: Visible focus ring with ≥3:1 contrast, encompassing entire control group ([Orange focus guidelines](https://a11y-guidelines.orange.com/en/web/design/navigation-focus/#make-focus-visible))
- [ ] **Error styling**: Red border + icon + text message—never color alone
- [ ] **Touch targets**: Buttons meet 44×44px minimum touch target size on mobile

### Content
- [ ] **Error messages**: ❌ "Invalid" / ✅ "Enter a quantity between 1 and 99" ([Orange error guidelines](https://a11y-guidelines.orange.com/en/web/components-examples/forms/))
- [ ] **Value context**: Include units in `aria-valuetext` when helpful (e.g., "5 items")