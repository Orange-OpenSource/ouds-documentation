# Bullet list — do & don't propositions

AI-generated propositions that no one has validated yet. They are not part of the documentation ([bullet_list.md](bullet_list.md)) and are not shown on zeroheight. Once a designer validates one, it moves into the full file.

## When to use

✅ To group related text items in a clear, structured format

✅ When content needs to be easy to scan and read

✅ For presenting mostly static, non-interactive information

✅ When items require a specific order (ordered) or no order at all (unordered / unstyled)

## Type — do & don't

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

## Text style — do & don't

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

## Nested level — do & don't

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

## Other boolean options — do & don't

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
