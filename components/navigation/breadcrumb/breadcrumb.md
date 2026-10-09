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

# Changelog

| Date | Number | Notes | Designer |
|------|--------|-------|----------|
| Oct 10, 2025 | 1.1.0 | • Update of the component token value: ouds-💠_navigation-breadcrumb-space-column-gap-links (visual render from 8px to 4px) • Removal of the component token: ouds-💠_navigation-breadcrumb-space-column-gap-icon • Update of the layer name from "Chevron" to "Icon" | Maxime Tonnerre |
| Fev 14, 2025 | 1.0.0 | • Component creation | Maxime Tonnerre |