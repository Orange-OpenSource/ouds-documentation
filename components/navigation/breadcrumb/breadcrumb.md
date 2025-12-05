# Guideline

## Intro 👈🤖

Breadcrumbs display a hierarchical navigation path, helping users understand their location and navigate back to previous pages.

---

## Definition

Breadcrumbs are a navigational aid that displays a hierarchical path, helping users understand their location and easily navigate back to previous pages.

---

## Best for 👈🤔

✅ Multi-level site architectures with more than two hierarchy levels

✅ E-commerce product pages requiring category context

✅ Documentation sites with nested content structures

✅ Content management systems with deep folder hierarchies

✅ Enterprise applications with complex information architecture

✅ Help center or support portals with categorized articles

✅ Media libraries organized by taxonomy or collections

✅ Government or institutional sites with regulatory content structures

✅ Educational platforms with course and module hierarchies

✅ Search results pages where users need to return to filtered views

---

## Anatomy 👈🤖

| # | Element | Purpose | Optional |
|---|---------|---------|----------|
| 1 | Navigation container | Wraps breadcrumb trail with semantic `nav` element and `aria-label` | N |
| 2 | Previous page link | Interactive link directing users to parent-level pages | N |
| 3 | Separator icon | Visual divider (chevron) between breadcrumb items, hidden from screen readers | N |
| 4 | Current page label | Non-interactive text indicating the user's current location | N |
| 5 | Overflow menu | Truncates middle items when trail exceeds available space (combined) | Y |

---

## Drilldown

Breadcrumbs can be categorized into different levels based on their complexity and hierarchy.

**`N+1`** The first level beyond the home page.

**`N+2`** A subcategory or a more specific section.

**`N+3`** A deeper level of navigation, often product or content grouping.

**`N+4`** A more refined selection, like a product variant or article.

---

## drilldown_do_&_dont 👈🤔

✅ **Do:** Limit breadcrumb depth to 4-5 levels maximum; use overflow menus for deeper hierarchies  
❌ **Don't:** Display excessively long breadcrumb trails that wrap to multiple lines

✅ **Do:** Show the full path on desktop and collapse to parent-only on mobile devices  
❌ **Don't:** Hide all hierarchy context on smaller screens, leaving users disoriented

✅ **Do:** Use consistent drilldown levels across similar content types within your site  
❌ **Don't:** Mix different hierarchy structures arbitrarily across the same product area

✅ **Do:** Ensure each level label accurately represents the page content it links to  
❌ **Don't:** Use vague or generic labels like "Category" or "Page" that don't provide context

✅ **Do:** Maintain logical parent-child relationships that match your site's information architecture  
❌ **Don't:** Skip hierarchy levels or create breadcrumb paths that don't reflect actual navigation structure

---

# Specs

## States

🚧 Missing from source: States section in breadcrumb_overview.md

---

## Layout and spacing

🚧 Content to be added

---

# Accessibility 👈🤖

## Accessibility intro

Breadcrumbs must be keyboard accessible, properly labeled for assistive technologies, and follow WCAG 2.2 AA guidelines for navigation landmarks. For comprehensive accessibility guidance, see the [Orange Unified Design System Accessibility Overview](https://unified-design-system.orange.com/472794e18/p/88ebab-accessibility-and-sustainability).

---

## Accessibility Challenges

Breadcrumbs present unique accessibility challenges as a secondary navigation pattern that must communicate hierarchical position without interfering with primary navigation or overwhelming screen reader users with repetitive announcements.

### Key Challenges
- Distinguishing breadcrumbs from primary navigation for screen reader users
- Communicating current page location without making it focusable as a dead link
- Ensuring separator icons don't create confusing announcements
- Managing long breadcrumb trails that may cause cognitive overload

### Critical Success Factors
1. Use `nav` element with descriptive `aria-label="Breadcrumb"` to identify the landmark
2. Mark current page with `aria-current="page"` attribute (WCAG 1.3.1)
3. Hide visual separators from assistive technology using `aria-hidden="true"` or CSS-only methods
4. Ensure all interactive links have minimum 44×44px touch targets (WCAG 2.5.5)

---

## Design Requirements

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

---

## Testing Checklist

### Screen Reader Testing
- [ ] Test with NVDA (Windows), JAWS (Windows), VoiceOver (macOS/iOS), TalkBack (Android)
- [ ] Verify: landmark announced as "Breadcrumb navigation", links announced with names, current page identified

### Keyboard Testing
- [ ] Tab navigates through all breadcrumb links in logical order, Enter activates links
- [ ] Focus indicator visible on each link with sufficient contrast

Resources: [Orange Accessibility Testing Guide](https://a11y-guidelines.orange.com/en/web/test/)

---

## Key WCAG Criteria

- **1.3.1 Info and Relationships** (A): Breadcrumb structure conveyed through semantic HTML and ARIA attributes
- **2.1.1 Keyboard** (A): All breadcrumb links operable via keyboard without timing requirements
- **2.4.4 Link Purpose** (A): Each breadcrumb link's purpose clear from link text alone
- **2.4.7 Focus Visible** (AA): Visible focus indicator on all interactive breadcrumb links
- **4.1.2 Name, Role, Value** (A): Navigation role, accessible names, and current state programmatically exposed

For complete reference: [Orange Accessibility Guidelines - Navigation](https://a11y-guidelines.orange.com/en/web/components-examples/)

---

## Additional Resources

- [W3C WAI-ARIA Breadcrumb Pattern](https://www.w3.org/WAI/ARIA/apg/patterns/breadcrumb/)
- [WCAG 2.2 Technique G65: Providing a breadcrumb trail](https://www.w3.org/TR/WCAG20-TECHS/G65.html)
- [Orange Accessibility Guidelines - Navigation Components](https://a11y-guidelines.orange.com/en/web/components-examples/)
- [Orange Design System - Accessibility & Sustainability](https://unified-design-system.orange.com/472794e18/p/88ebab-accessibility-and-sustainability)

---

# Changelog

| Date | Number | Notes | Designer |
|------|--------|-------|----------|
| Oct 10, 2025 | 1.1.0 | • Update of the component token value: ouds-💠_navigation-breadcrumb-space-column-gap-links (visual render from 8px to 4px) • Removal of the component token: ouds-💠_navigation-breadcrumb-space-column-gap-icon • Update of the layer name from "Chevron" to "Icon" | Maxime Tonnerre |
| Fev 14, 2025 | 1.0.0 | • Component creation | Maxime Tonnerre |