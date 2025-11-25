### Structure & Labels
- [ ] **Visible labels required**: Every text area must have a permanently visible label positioned above the field, not just placeholder text ([Orange Forms Guidelines](https://a11y-guidelines.orange.com/en/web/develop/forms/))
- [ ] **Programmatic association**: Use `<label for="id">` pointing to text area's `id` attribute to create proper association for assistive technology
- [ ] **Helper text association**: Connect helper text using `aria-describedby` to ensure screen readers announce it when the field receives focus