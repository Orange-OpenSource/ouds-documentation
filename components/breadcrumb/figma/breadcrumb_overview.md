## Definition

A breadcrumb is a UI element that aids in navigation and identifies the current location on a website by displaying a hierarchical path of web pages.

---

## Drilldown

Breadcrumbs can be categorized into different levels based on their complexity and hierarchy. The current page is never interactive.

**`N+1`** The first level beyond the home page.

**`N+2`** A subcategory or a more specific section.

**`N+3`** A deeper level of navigation, often product or content grouping.

**`N+4`** A more refined selection, like a product variant or article.

---

## Display rule

The general display rule is: Depending on the screen width (breakpoint), we hierarchically hide page names by prioritizing the display of the currently viewed page back to the homepage.
We prioritize displaying the name of the currently viewed page, then the previous page, and so on, up to displaying the homepage name if the screen width allows it.

At a minimum, and for all breakpoints, the currently viewed page and page n-1 (the page preceding the currently viewed page) are always displayed.
Depending on the breakpoints, the number of pages shown or hidden changes:
- 2xs, xs, sm: 2 names max -> Previous / Current
- md: 3 names max -> Previous / Previous / Current
- lg: 4 names max -> Previous / Previous / Previous / Current
- xl, 2xl, 3xl: The entire hierarchy is displayed

Note that technically (CSS helper classes) and depending on the breakpoint, it is possible to force the specific display of a page that is not shown by default, and vice versa.

Except for the name of page n-1, which is never truncated, the names of the other pages may be truncated (from the homepage to the currently viewed page inclusive).
Note that technically (CSS helper classes), we retain the ability not to truncate the display of a specific page (for example, we prefer not to truncate the homepage name).

---

## Multiline and responsiveness

**Multiline**
This component doesn't allows multi-line text editing.

**Max-width**
For greater flexibility, this component doesn't have a max-width.

**User zoom in/out**
The behavior of the text during user zoom in/out must follow a fundamental principle: the text must remain readable, accessible, and must never break the structure or lose information.
- The text must always scale proportionally with user zoom. Text resizing must never be blocked.
- Except for the name of page n-1, which is never truncated, and for this specific component, zooming may cause text to be truncated or hidden. The component must expand vertically to allow line wrapping.
- The component's height and width must be flexible, never fixed, in order to automatically adapt its dimensions according to the level of zoom.
- In order to preserve the minimun interactive area during user zoom out or during page name truncation, each link have a min-width and a min-height of 44px.
- Even if, the component has a max-height or a max-width for resizing control purposes, technically, during user zoom in, these limitations are not fixed but must be scalable in order to adapt to the user's zoom level.
- Even with user zoom in/out, this component does not allow multi-line text editing. As a result, the component may end up with horizontal scrolling if the total width of the non-truncatable labels exceeds the width of the container or the page.
- As the chevron icon is functional, it must follow the same rules as text.
