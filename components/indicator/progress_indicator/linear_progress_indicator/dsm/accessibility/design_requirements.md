### Structure & Labels
- [ ] **Role & name**: Expose `role="progressbar"` with an accessible name describing what is loading ([Orange A11y guidelines](https://a11y-guidelines.orange.com/en/web/components-examples/))
- [ ] **Determinate value**: Provide `aria-valuenow`, `aria-valuemin`, `aria-valuemax`; use `aria-valuetext` for human-readable progress
- [ ] **Indeterminate**: Omit `aria-valuenow` so assistive tech announces an unspecified wait

### Visual Design
- [ ] **Non-text contrast**: Indicator/track meet ≥3:1 against their background ([Link](https://a11y-guidelines.orange.com/en/articles/contrasts/))
- [ ] **Status not by color alone**: Pair functional statuses with text or context (1.4.1)
- [ ] **Zoom & reflow**: Bar and helper text stay clear and readable up to 200% (1.4.4, 1.4.10)

### Content
- [ ] **Meaningful announcement**: ❌ "1, 2, 3, 4…" / ✅ "Uploading file, 40 percent complete" ([Link](https://a11y-guidelines.orange.com/en/web/components-examples/))
- [ ] **Localized percentage**: Respect the locale's space-before-% rule (40 % in French)