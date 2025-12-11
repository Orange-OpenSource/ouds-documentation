### Structure & Labels
- [ ] **Accessible name**: Provide `aria-label="Previous page"` or `aria-label="Next page"` for icon-only buttons ([Orange A11y - Form Buttons](https://a11y-guidelines.orange.com/en/web/develop/form-buttons/))
- [ ] **Button semantics**: Use native `<button>` element, not links or divs with click handlers
- [ ] **Disabled communication**: Apply `aria-disabled="true"` and `disabled` attribute when on first/last page

### Visual Design
- [ ] **Focus indicator**: Visible focus ring with ≥3:1 contrast against adjacent colors ([Orange A11y - Focus Visibility](https://a11y-guidelines.orange.com/en/web/design/focus-visibility/))
- [ ] **Touch target**: Minimum 44×44px interactive area for all button variants
- [ ] **Color contrast**: Text/icon ≥4.5:1, UI boundaries ≥3:1 against background

### Content
- [ ] **Clear labeling**: ❌ ">" / ✅ "Next page" for accessible name ([Orange A11y - Link and Button Labels](https://a11y-guidelines.orange.com/en/web/design/link-button-labels/))
- [ ] **Loading announcement**: Include `aria-live="polite"` for loading state changes