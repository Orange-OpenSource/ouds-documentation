### Structure & Labels
- [ ] **Visible labels required**: Every text area must have a permanently visible label positioned above the field, not just placeholder text ([Orange Forms Guidelines](https://a11y-guidelines.orange.com/en/web/develop/forms/))
- [ ] **Programmatic association**: Use `<label for="id">` pointing to text area's `id` attribute to create proper association for assistive technology
- [ ] **Helper text association**: Connect helper text using `aria-describedby` to ensure screen readers announce it when the field receives focus

### Visual Design
- [ ] **Focus indicators**: Provide visible focus state with ≥3:1 contrast ratio against adjacent colors, never remove or hide focus outlines ([WCAG 2.4.7](https://www.w3.org/WAI/WCAG22/Understanding/focus-visible))
- [ ] **Color contrast**: Ensure text and borders meet 4.5:1 for normal text, 3:1 for large text and UI components ([WCAG 1.4.3, 1.4.11](https://a11y-guidelines.orange.com/en/web/develop/forms/))
- [ ] **Clear boundaries**: Text area borders must be clearly visible with sufficient contrast to indicate the input region

### Content
- [ ] **Descriptive labels**: ❌ "Comments" / ✅ "Please describe the issue you experienced" ([Orange Forms Best Practices](https://a11y-guidelines.orange.com/en/web/develop/forms/))
- [ ] **Clear error messages**: Explain what went wrong and how to fix it without technical jargon, programmatically associated via `aria-describedby`
