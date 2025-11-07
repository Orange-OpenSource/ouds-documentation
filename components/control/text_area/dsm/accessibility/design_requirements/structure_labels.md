### Structure & Labels
<<<<<<< HEAD
- [ ] **Label association**: Every text area has a visible `<label>` element programmatically linked using `for`/`id` attributes ([Orange Forms Guidelines](https://a11y-guidelines.orange.com/en/web/components-examples/forms/))
- [ ] **Helper text linking**: Character counter and helper text associated with input using `aria-describedby` attribute referencing their IDs
- [ ] **Error message connection**: Error messages must be associated via `aria-describedby` (in addition to label/helper text IDs) and announced when error state changes
=======
<<<<<<< Updated upstream
- [ ] **Programmatically associated label**: Connect visible label to `<textarea>` via `id` and `for` attribute, never omit even if visually hidden ([Orange A11y - Forms](https://a11y-guidelines.orange.com/en/web/components-examples/forms/))
- [ ] **Multi-ID aria-describedby**: Associate helper text, character counter, and error message using space-separated IDs so screen readers announce all context
- [ ] **Persistent label visibility**: Keep labels visible by default unless placeholder + context icon clearly convey purpose with hidden label still available to assistive technology
>>>>>>> c9e8b9e (content: update)