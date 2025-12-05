### Structure & Labels
- [ ] **Navigation landmark**: Wrap in `nav` element with `aria-label="Breadcrumb"` ([Orange landmark guidelines](https://a11y-guidelines.orange.com/en/web/develop/landmarks/))
- [ ] **Semantic list**: Use `ol` with `li` for each item to convey hierarchy to assistive technologies
- [ ] **Current page indicator**: Apply `aria-current="page"` to the last item representing current location

### Visual Design
- [ ] **Focus indicator**: Visible focus state with ≥3:1 contrast ratio against background ([Orange focus guidelines](https://a11y-guidelines.orange.com/en/web/design/focus/))
- [ ] **Link contrast**: Text links meet 4.5:1 minimum contrast ratio against background
- [ ] **Touch targets**: Interactive links have minimum 44×44px target size for touch accessibility

### Content
- [ ] **Link labels**: ❌ "Click here" / ✅ "Products" — use descriptive, concise page names ([Orange link guidelines](https://a11y-guidelines.orange.com/en/web/develop/links/))
- [ ] **Separator hiding**: Visual separators hidden from screen readers via `aria-hidden="true"` or CSS