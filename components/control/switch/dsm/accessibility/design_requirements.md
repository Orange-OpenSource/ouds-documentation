### Structure & Labels
- [ ] **Programmatic label**: Associate visible label with switch using `for`/`id` or `aria-labelledby` ([Orange Forms Guide](https://a11y-guidelines.orange.com/en/web/develop/forms/))
- [ ] **Role and state**: Use `role="switch"` with `aria-checked="true|false"` to communicate state
- [ ] **Error association**: Link error messages via `aria-describedby` when in error state

### Visual Design
- [ ] **Focus indicator**: Visible focus ring with ≥3:1 contrast ratio ([Focus Guidelines](https://a11y-guidelines.orange.com/en/web/design/colors-and-contrasts/#make-sure-there-is-enough-contrast-between-the-colors))
- [ ] **State differentiation**: Use position, color, AND icon to indicate on/off (not color alone)
- [ ] **Touch target**: Minimum 48×48px interactive area for touch accessibility

### Content
- [ ] **Clear labels**: ❌ "Enable" / ✅ "Enable notifications for new messages"
- [ ] **Actionable errors**: Error text must explain how to resolve the issue