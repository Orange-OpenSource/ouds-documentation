### Structure & Labels
- [ ] **Group label**: Provide a visible label for the entire PIN input group using `<fieldset>` and `<legend>` or `aria-labelledby`
- [ ] **Individual labels**: Label each digit field with its position (visually hidden: "Digit 1 of 6") ([Orange Label Guidelines](https://a11y-guidelines.orange.com/en/web/develop/text-alternatives/))
- [ ] **Live regions**: Use `aria-live="polite"` to announce focus changes and completion status

### Visual Design
- [ ] **Focus indicator**: Visible focus with ≥3:1 contrast ratio and ≥2px outline ([Orange Focus Guidelines](https://a11y-guidelines.orange.com/en/web/design/focus/))
- [ ] **Error styling**: Error state uses color plus icon/border, never color alone (WCAG 1.4.1)
- [ ] **Touch targets**: Each digit field minimum 44×44px on touch devices

### Content
- [ ] **Error messages**: ❌ "Error" / ✅ "Incorrect code. Please check your SMS and try again." ([Orange Error Guidelines](https://a11y-guidelines.orange.com/en/web/develop/forms/#errors))
- [ ] **Instructions**: Provide clear helper text explaining expected format and code source