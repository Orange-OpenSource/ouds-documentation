# Guideline

## Intro 👈🤖

Bullet List displays related text items in a structured vertical format using bullets, numbers, or no markers.

---

## Definition

List allows users to view individual, but related, text items grouped together.

It usually begins with either a number or a bullet, also known as Unordered list or Ordered list.

By default, **this component is not interactive**, although it is possible to add a hypertext link to the content.

---

## Best for 👈🤔

✅ Displaying non-sequential related items without implied priority or order

✅ Presenting step-by-step instructions or sequential procedures requiring numbered order

✅ Grouping features, benefits, or options for easy scanning and comparison

✅ Breaking up dense paragraph content into digestible chunks for improved readability

✅ Creating navigation menus or table of contents with hierarchical structure

✅ Listing requirements, specifications, or criteria in technical documentation

✅ Showing checklists or task lists in forms and workflows

✅ Presenting terms and conditions, policies, or legal information

✅ Organizing FAQ content with clear structure and visual separation

✅ Displaying nested categorization with parent-child relationships up to three levels

---

## Anatomy 👈🤖

| # | Element | Purpose | Optional |
|---|---------|---------|----------|
| 1 | Marker/Bullet | Visual indicator distinguishing list type (square, dash, number, letter) | N |
| 2 | Label/Content | Primary text content of the list item | N |
| 3 | Icon container | Wrapper for bullet icons ensuring proper alignment | N |
| 4 | Nested indentation | Left padding indicating hierarchy level (Level 0, 1, 2) | Y |
| 5 | Hyperlink | Optional interactive link within list content | Y |
| 6 | Skeleton loader | Loading placeholder shown during content fetch | Y |

---

## Type

**`Unordered`** Collects related items that don't need to be in a specific order or sequence. List items are typically marked with bullets, but it is also possible to use a tick or any Solaris icon.

**`Ordered`** Collects related items with numeric order or sequence. Numbering starts at 1 with the first list item and increases by increments of 1 for each successive ordered list item.

**`Bare`** An unordered list without any bullets or alphanumeric sequence. It still have left-padding, so list items will appear indented. This is the default and is also known as undecorated "Unstyled" list.

---

## type_do_&_dont 👈🤔

✅ **Do:** Use unordered lists when items are of equal value and order doesn't matter  
❌ **Don't:** Use ordered lists for content that has no sequential relationship

✅ **Do:** Use ordered lists for step-by-step instructions, rankings, or prioritized content  
❌ **Don't:** Use bullets for procedures where steps must be followed in a specific sequence

✅ **Do:** Use bare lists when you need list semantics without visual markers for navigation or layout  
❌ **Don't:** Remove list markers purely for aesthetic reasons without considering accessibility impact

✅ **Do:** Choose list type based on content meaning, not visual preference  
❌ **Don't:** Mix list types inconsistently within the same content section

✅ **Do:** Consider screen reader announcements when selecting list type ("bullet" vs. numbered)  
❌ **Don't:** Use bare lists when users need markers to understand item relationships

---

## Text style

List can be used with different font sizes, these sizes are based on our body font-size.
Today, list is available with two text styles: Body large and body Medium.

**`Body Large`** Make sure to use this reference if the text accompanying the list component is the Body Large text.
This variant is designed for more visual, engaging experiences.

**`Body Medium`** Make sure to use this reference if the text accompanying the list component is the Body Medium text.
This variant is best suited for functional, task-oriented experiences.

---

## text_style_do_&_dont 👈🤔

✅ **Do:** Match list text style to the surrounding body text for visual consistency  
❌ **Don't:** Use Body Large lists within Body Medium paragraph content

✅ **Do:** Use Body Large for marketing pages, landing pages, and editorial content  
❌ **Don't:** Use Body Large in compact data-dense interfaces where space is limited

✅ **Do:** Use Body Medium for forms, dashboards, and functional UI with task focus  
❌ **Don't:** Mix Body Large and Body Medium text styles within the same list

✅ **Do:** Consider the reading context and viewport size when selecting text style  
❌ **Don't:** Choose text style solely based on aesthetic preference over usability

✅ **Do:** Ensure sufficient line-height for readability at the chosen text size  
❌ **Don't:** Reduce spacing between items to the point of compromising scannability

---

## Nested level

Lists can include nested items to indicate hierarchy or subcategories, with indentation distinguishing each level. Arrange ordered list items logically, such as ranking by importance, highest to lowest values, or in alphabetical/numeric order.

**`Nested level: 0`** Level 0 list items define the main structure.
Unordered level 0 list items are marked with full squares.
Ordered level 0 list items are marked with numbers.

**`Nested level: 1`** Level 1 (nested) list items provide hierarchy or subcategories.
Unordered level 1 list items are marked with outlined squares.
Ordered level 1 list items are marked with uppercase letters.

**`Nested level: 2`** Level 2 (nested) list items provide hierarchy or subcategories.
Unordered level 2 list items are marked with dashes.
Ordered level 2 list items are marked with lowercase letters.

Ordered lists can be combined with unordered items in the same list as well.

Note that, in this context, even though the Unordered list item is placed at nested level 1, it is rendered as if it were at nested level 0 (full square) because, in the technical implementation, **the combination of Ordered and Unordered lists is not incremental.**

Conversely, **in a context using only Unordered lists, the incrementing does apply** even if the choice of nested items differs (bullet items with ticks or Solairs icons).

In the technical implementation, **Bar lists are considered as Unordered lists**. The incrementing between lists does apply.

---

## nested_level_do_&_dont 👈🤔

✅ **Do:** Limit nesting to a maximum of 2-3 levels to maintain readability and comprehension  
❌ **Don't:** Create deeply nested lists (4+ levels) that become difficult to scan

✅ **Do:** Use distinct visual markers at each nesting level for clear hierarchy differentiation  
❌ **Don't:** Use identical markers across nesting levels causing visual confusion

✅ **Do:** Ensure proper indentation spacing to clearly distinguish parent-child relationships  
❌ **Don't:** Use minimal indentation that makes hierarchy relationships unclear

✅ **Do:** Group related sub-items logically under their parent category  
❌ **Don't:** Nest unrelated items together just to reduce vertical space

✅ **Do:** Consider flattening deeply nested structures into separate lists with headings  
❌ **Don't:** Force complex hierarchies into a single nested list when sections work better

---

## Other boolean options

**`Bold`** The label text can be bolded.

**`Skeleton`** Improves the perceived loading time by providing a visual cue of where switch will appear once fully loaded.
Uses the "Skeleton" component, variant "Security marge=True".

Even if the "Bold" option is not active, it is also possible to add a hyperlink in the content of a list. In terms of design, and depending on the chosen text style, the typographic reference "Body/Large/Underline" or "Body/Medium/Underline" must be used.

---

## other_boolean_options_do_&_dont 👈🤔

✅ **Do:** Use bold text sparingly to emphasize key terms or important items within lists  
❌ **Don't:** Bold entire list items as it reduces the emphasis effect and impacts readability

✅ **Do:** Use skeleton loaders when list content requires async data fetching  
❌ **Don't:** Show skeleton loaders for static content that loads immediately

✅ **Do:** Style hyperlinks consistently using the appropriate underline typography reference  
❌ **Don't:** Remove underlines from links as it reduces accessibility and discoverability

✅ **Do:** Ensure hyperlinks have sufficient color contrast and clear hover/focus states  
❌ **Don't:** Use link styling on non-interactive text elements

✅ **Do:** Keep skeleton dimensions consistent with the expected loaded content  
❌ **Don't:** Use skeleton heights that cause significant layout shift when content loads

---

# Specs

## States

🚧 Missing from source: States section in bullet_list_overview.md

---

## Layout and spacing

🚧 Content to be added

---

# Changelog

| Date | Number | Notes | Designer |
|------|--------|-------|----------|
| Mar 26, 2025 | 1.0.0 | • Component creation | Maxime Tonnerre |