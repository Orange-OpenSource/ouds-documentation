### Structure & Labels
- [ ] **Visible label**: Always provide a visible text label; if hidden, use visually-hidden CSS with `aria-label` or `aria-labelledby`
- [ ] **Programmatic association**: Label connected via `for`/`id` pairing ([Orange: Form labels](https://a11y-guidelines.orange.com/en/web/develop/forms/))
- [ ] **Helper text connection**: Password requirements linked via `aria-describedby` on the input element

### Visual Design
- [ ] **Focus indicator**: 2px solid outline with ≥3:1 contrast against adjacent colors
- [ ] **Toggle button contrast**: Show/hide icon or text meets 3:1 contrast against background ([Color contrast](https://a11y-guidelines.orange.com/en/web/design/colors-and-contrasts/))
- [ ] **Error styling**: Red border with error icon; never rely on color alone to indicate errors

### Content
- [ ] **Error messages**: ❌ "Invalid password" / ✅ "Password must be at least 8 characters"
- [ ] **Toggle labels**: Use clear text ("Show password" / "Hide password") or accessible icon with `aria-label`