### Structure & Labels
- [ ] **Visible label**: Always provide a persistent visible label; never use placeholder as sole label ([Orange Label Guidelines](https://a11y-guidelines.orange.com/en/web/components-examples/forms/))
- [ ] **Programmatic association**: Connect labels to inputs via `for`/`id` attributes or implicit wrapping
- [ ] **Required indication**: Communicate required status via `aria-required="true"` and visual indicator with legend

### Visual Design
- [ ] **Focus indicator**: Provide visible focus state with ≥3:1 contrast against adjacent colors ([Orange Focus Guidelines](https://a11y-guidelines.orange.com/en/web/))
- [ ] **Error styling**: Use multiple cues for errors: red border, error icon, and text message—not color alone
- [ ] **Contrast ratios**: Input text ≥4.5:1; placeholder text ≥4.5:1; borders ≥3:1 against background

### Content
- [ ] **Error messages**: ❌ "Invalid" / ✅ "Enter a valid email address (e.g., name@example.com)" ([Orange Error Guidelines](https://a11y-guidelines.orange.com/en/web/components-examples/forms/))
- [ ] **Helper text**: Keep concise; associate with input via `aria-describedby` for screen reader announcement