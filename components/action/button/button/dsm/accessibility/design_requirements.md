### Structure & Labels

- [ ] **Semantic HTML**: Use native `<button>` element; avoid `<div>` or `<span>` with click handlers ([Orange Forms Guidelines](https://a11y-guidelines.orange.com/en/web/components-examples/forms/))
- [ ] **Accessible names**: All buttons must have discernible text via visible label or `aria-label`
- [ ] **Icon-only labeling**: Provide `aria-label` and tooltip for icon-only variants

### Visual Design

- [ ] **Focus indicator**: Visible focus ring with ≥3:1 contrast ratio against adjacent colors ([Orange Focus Guidelines](https://a11y-guidelines.orange.com/en/web/design/colors-and-contrasts/#focus-visibility))
- [ ] **Text contrast**: Button text must have ≥4.5:1 contrast against button background
- [ ] **Disabled styling**: Use reduced opacity (0.28) and `aria-disabled="true"`; avoid `disabled` attribute when possible

### Content

- [ ] **Button labels**: Use action verbs (Save, Submit, Delete); ❌ "Click here" / ✅ "Submit form"
- [ ] **Concise text**: Keep labels under 3 words when possible; avoid truncation