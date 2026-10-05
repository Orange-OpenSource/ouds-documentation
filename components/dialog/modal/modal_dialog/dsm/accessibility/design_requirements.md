### Structure & Labels

- [ ] **Accessible name**: The title is always displayed and is referenced by `aria-labelledby`; a short description by `aria-describedby` (omit it when the content holds lists, tables or several paragraphs)
- [ ] **Initial focus**: The most likely-used element by default, the least destructive action for irreversible choices, the title or a top element when the content is long
- [ ] **Close button**: The icon-only Close button has an accessible name such as `aria-label="Close"` ([Orange ARIA guidelines](https://a11y-guidelines.orange.com/en/web/develop/textual-content/))

### Visual Design

- [ ] **Focus indicator**: 3:1 minimum contrast ratio with ≥2px visible border on every interactive element ([Focus visibility](https://a11y-guidelines.orange.com/en/web/design/focus-visibility/))
- [ ] **Text contrast**: Title, subtitle and description meet 4.5:1 against the container; the Close icon and status icons meet 3:1
- [ ] **Reflow and zoom**: At 200% zoom and 320 px width the content scrolls inside the dialog and the actions remain reachable

### Content

- [ ] **Clear title**: ❌ "Warning" / ✅ "Delete this document?" ([Clear labels](https://a11y-guidelines.orange.com/en/web/design/content/))
- [ ] **Explicit actions**: Action labels name the outcome and stay understandable out of context
- [ ] **Status not by colour alone**: Negative and positive meanings are carried by the text; a status Title icon has a text alternative, a decorative one is hidden