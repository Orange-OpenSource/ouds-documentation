# Guideline

## Intro 👈🤖

A divider is a thin visual line that separates and organizes content sections to improve readability and interface structure.

---

## Definition

A Divider is a UI component used to visually structure an interface by clearly separating content sections. It helps improve readability and content organization without introducing a strong hierarchy like a heading or a container would.

---

## Best for 👈🤔

✅ Separating stacked content sections vertically (e.g., between main content and footer)

✅ Dividing horizontally aligned elements (e.g., between columns in a layout)

✅ Grouping related menu items or navigation options

✅ Creating visual breaks between list items in dense content

✅ Separating form sections without adding hierarchical weight

✅ Distinguishing content areas within cards or panels

✅ Breaking up long scrolling pages into scannable sections

✅ Separating toolbar actions or icon groups

✅ Creating thematic breaks between paragraphs or articles

✅ Visually organizing dashboard widgets or data regions

---

## Anatomy 👈🤖

| # | Element | Purpose | Optional |
|---|---------|---------|----------|
| 1 | Line | The visual separator element that creates the division between content sections | N |
| 2 | Container | The bounding area that controls the divider's dimensions and positioning | N |
| 3 | Spacing | Margin or padding around the divider that creates visual breathing room | Y |
| 4 | Color | The stroke color applied to the line, using design tokens for consistency | N |
| 5 | Thickness | The stroke weight of the divider line (typically 1px) | N |

---

## Orientation

**`Horizontal`** Separates stacked vertical sections. Example use case: Between main content and a footer.

**`Vertical`** Separates horizontally aligned elements. Example use case: Between two columns in a layout.

---

## orientation_do_&_dont 👈🤔

✅ **Do:** Use horizontal dividers to separate stacked content sections that flow vertically down the page  
❌ **Don't:** Use horizontal dividers between side-by-side elements that should be separated vertically

✅ **Do:** Use vertical dividers in flex containers or toolbars to separate grouped inline elements  
❌ **Don't:** Use vertical dividers to separate content that flows vertically—use horizontal dividers instead

✅ **Do:** Ensure vertical dividers have sufficient height by using `flexItem` or explicit height in flex containers  
❌ **Don't:** Place vertical dividers in block-level contexts where they collapse to zero height

✅ **Do:** Match the divider orientation to the layout direction—horizontal for vertical stacks, vertical for horizontal rows  
❌ **Don't:** Mix orientations inconsistently within the same UI pattern or component

✅ **Do:** Set `aria-orientation` appropriately when using custom divider implementations  
❌ **Don't:** Rely on default horizontal orientation when rendering a vertical divider—explicitly declare it

---

## Authorized colors

• color-border-default
• color-border-muted
• color-border-emphasized
• color-border-brand-primary (secondary/tertiary)
• color-border-on-brand-primary (secondary/tertiary)
• color-always-black
• color-always-white
• color-always-on-black
• color-always-on-white

---

## authorized_colors_do_&_dont 👈🤔

✅ **Do:** Use `color-border-default` or `color-border-muted` for standard content separation  
❌ **Don't:** Use strong or vibrant colors that draw attention away from the content being separated

✅ **Do:** Use brand colors (`color-border-brand-primary`) sparingly for intentional visual emphasis  
❌ **Don't:** Apply brand colors to every divider—reserve them for specific branding contexts

✅ **Do:** Use `color-always-white` or `color-always-on-black` when placing dividers on dark backgrounds  
❌ **Don't:** Use dark divider colors on dark backgrounds where contrast would be insufficient

✅ **Do:** Maintain consistent divider colors throughout similar UI patterns and contexts  
❌ **Don't:** Vary divider colors arbitrarily within the same interface section

✅ **Do:** Ensure divider color meets minimum contrast requirements against adjacent backgrounds  
❌ **Don't:** Use colors that blend into the background, making the divider invisible or hard to perceive

---

# Specs

## States

🚧 Missing from source: States section in divider_overview.md

---

## Layout and spacing

🚧 Content to be added

---

# Changelog

| Date | Number | Notes | Designer |
|------|--------|-------|----------|
| Mar 14, 2025 | 1.0.0 | • Component creation | Anton Astafev |