### Structure & Labels

- [ ] **Semantic role**: Use `role="alert"` for urgent messages, `role="status"` for non-urgent ([Orange A11y - ARIA](https://a11y-guidelines.orange.com/en/web/develop/rich-interface-components/))
- [ ] **Status text**: Include visible text label alongside icon to communicate status to all users
- [ ] **Accessible name**: Close button must have accessible name (e.g., `aria-label="Dismiss alert"`)

### Visual Design

- [ ] **Text contrast**: Minimum 4.5:1 contrast ratio for body text against background ([Orange A11y - Colors](https://a11y-guidelines.orange.com/en/web/design/colors-and-contrasts/))
- [ ] **Focus indicator**: Visible focus ring with ≥3:1 contrast on close button and action links
- [ ] **Non-color indicators**: Status communicated via icon + text, not color alone

### Content

- [ ] **Descriptive actions**: ❌ "Click here" / ✅ "View account settings" ([Orange A11y - Links](https://a11y-guidelines.orange.com/en/web/design/navigation/))
- [ ] **Concise messages**: Keep alert text scannable; link to details for complex information