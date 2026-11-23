# Link — do & don't propositions

AI-generated propositions that no one has validated yet. They are not part of the documentation ([link.md](link.md)) and are not shown on zeroheight. Once a designer validates one, it moves into the full file.

## When to use

✅ When navigation between pages, sections, or external resources is required

✅ For inline navigation within text or content-heavy layouts

✅ When the primary purpose is navigation, not triggering an action

✅ To provide a clear, lightweight path to additional information

## Layouts — do & don't

✅ **Do:** Use the "Next" layout for forward navigation in sequential flows like wizards or multi-step processes  
❌ **Don't:** Use chevron layouts for inline text links embedded within paragraphs

✅ **Do:** Reserve the "Visited" layout for contexts where tracking navigation history adds value, such as search results  
❌ **Don't:** Apply visited styles universally as they can create visual clutter and confusion

✅ **Do:** Match the "Text + icon" layout with icons that reinforce the link's destination or purpose  
❌ **Don't:** Use decorative icons that don't provide meaningful context about the link destination

✅ **Do:** Use "Text only" layout for inline links within body copy to maintain reading flow  
❌ **Don't:** Pair inline text links with icons as this disrupts the reading experience

✅ **Do:** Use "Previous" layout consistently for returning to previous pages or steps in a flow  
❌ **Don't:** Mix "Previous" and "Next" layouts inconsistently within the same navigation context

## Sizes — do & don't

✅ **Do:** Match inline link size to the surrounding body text size for visual consistency  
❌ **Don't:** Use mismatched link sizes that create jarring visual hierarchies within text blocks

✅ **Do:** Use the small size variant in dense interfaces like data tables, sidebars, or compact cards  
❌ **Don't:** Use small links as primary navigation elements where visibility is critical

✅ **Do:** Ensure small links maintain the minimum touch target size of 44×44px for mobile accessibility  
❌ **Don't:** Reduce link size below readable thresholds even in dense layouts

✅ **Do:** Use default size for standalone links that serve as primary navigation or calls-to-action  
❌ **Don't:** Mix multiple link sizes within the same navigation group or list

✅ **Do:** Consider the overall information density when selecting link size  
❌ **Don't:** Default to small size simply to fit more content on screen

## Specific component: On colored bg — do & don't

✅ **Do:** Use the "On colored bg" variant when placing links on brand colors, images, or gradients  
❌ **Don't:** Use standard link colors on colored backgrounds without checking contrast ratios

✅ **Do:** Test link visibility across all theme modes (light/dark) when using inverted color options  
❌ **Don't:** Assume one color configuration works for both light and dark modes

✅ **Do:** Ensure the inverted link color maintains a minimum 4.5:1 contrast ratio against the background  
❌ **Don't:** Use colored backgrounds that reduce link visibility below accessibility standards

✅ **Do:** Apply the "On colored bg" variant consistently across all link states (hover, focus, pressed)  
❌ **Don't:** Mix standard and inverted link variants on the same colored surface

✅ **Do:** Use black finish in light mode and white finish in dark mode for optimal readability  
❌ **Don't:** Invert colors arbitrarily without considering the overall visual hierarchy
