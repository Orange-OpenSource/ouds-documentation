### Structure & Labels
- [ ] **Visible label**: Persistent label text "Phone number" associated via `<label for="">` ([Orange label guidelines](https://a11y-guidelines.orange.com/en/web/components-examples/forms/))
- [ ] **Input type**: Use `type="tel"` and `autocomplete="tel"` for proper keyboard and autofill ([WCAG 1.3.5](https://www.w3.org/WAI/WCAG21/Understanding/identify-input-purpose.html))
- [ ] **Group labeling**: Wrap country selector and input in `role="group"` with descriptive `aria-label`

### Visual Design
- [ ] **Focus indicator**: Visible focus ring with ≥3:1 contrast ratio on all interactive elements ([Orange focus guidelines](https://a11y-guidelines.orange.com/en/web/design/colors-and-contrasts/))
- [ ] **Error styling**: Red border + error icon + text message, never color alone
- [ ] **Touch targets**: Minimum 44×44px for country selector button on mobile

### Content
- [ ] **Error messages**: ❌ "Invalid" / ✅ "Enter a 10-digit phone number" ([Orange error guidelines](https://a11y-guidelines.orange.com/en/web/components-examples/forms/))
- [ ] **Country list**: Include both country name and code for screen reader clarity