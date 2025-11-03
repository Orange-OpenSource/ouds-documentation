### Structure & Labels
- [ ] **Label association**: Every text area has a visible `<label>` element programmatically linked using `for`/`id` attributes ([Orange Forms Guidelines](https://a11y-guidelines.orange.com/en/web/components-examples/forms/))
- [ ] **Helper text linking**: Character counter and helper text associated with input using `aria-describedby` attribute referencing their IDs
- [ ] **Error message connection**: Error messages must be associated via `aria-describedby` (in addition to label/helper text IDs) and announced when error state changes