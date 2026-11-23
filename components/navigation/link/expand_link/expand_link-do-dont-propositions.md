# Expand link — do & don't propositions

AI-generated propositions that no one has validated yet. They are not part of the documentation ([expand_link.md](expand_link.md)) and are not shown on zeroheight. Once a designer validates one, it moves into the full file.

## When to use

✅ When revealing or hiding additional content inline without breaking the layout

✅ For secondary or optional information that doesn’t require a full button

✅ When minimal visual weight is important to maintain content focus

✅ In dense layouts where space efficiency and clarity matter

## Expanded — do & don't

✅ **Do:** Use clear, action-oriented labels like "Show details" or "View more" that indicate what will be revealed  
❌ **Don't:** Use vague labels like "Click here" or "More" that don't describe the hidden content

✅ **Do:** Animate the chevron icon rotation to provide visual feedback of state change  
❌ **Don't:** Change the icon abruptly without transition, which can disorient users

✅ **Do:** Maintain the expanded state when users navigate away and return to preserve context  
❌ **Don't:** Automatically collapse content on page revisit, forcing users to re-expand

✅ **Do:** Position expanded content directly below the trigger for clear visual association  
❌ **Don't:** Display revealed content far from the trigger, breaking the spatial relationship

✅ **Do:** Allow multiple expand links to be open simultaneously for user flexibility  
❌ **Don't:** Force accordion behavior (auto-collapse) unless content relationships require it

## Sizes — do & don't

✅ **Do:** Use the default size for standalone expand links in primary content areas  
❌ **Don't:** Mix different sizes of expand links within the same visual grouping

✅ **Do:** Use the small size within compact components like alerts, cards, or data tables  
❌ **Don't:** Use small size when the expand link is the primary action on a page

✅ **Do:** Ensure touch targets meet minimum 44×44px requirements regardless of visual size  
❌ **Don't:** Reduce the interactive area below accessibility guidelines for small size

✅ **Do:** Scale font size proportionally with the size variant using design tokens  
❌ **Don't:** Override typography tokens with fixed pixel values

✅ **Do:** Maintain consistent chevron icon proportions relative to label text  
❌ **Don't:** Use oversized or undersized icons that create visual imbalance

## Specific component: On colored bg — do & don't

✅ **Do:** Use the "On colored bg" variant when placing expand links on colored, image, or gradient backgrounds  
❌ **Don't:** Use the standard variant on backgrounds where contrast cannot be guaranteed

✅ **Do:** Test color contrast ratios meet WCAG AA (4.5:1 for text) in both light and dark modes  
❌ **Don't:** Assume the inverted variant will work without verifying actual contrast values

✅ **Do:** Apply consistent inverted color treatment to all interactive states (hover, focus, pressed)  
❌ **Don't:** Mix standard and inverted color schemes within the same background context

✅ **Do:** Use design tokens for color management to ensure automatic theme switching  
❌ **Don't:** Hard-code color values that won't adapt to light/dark mode changes

✅ **Do:** Ensure focus indicators remain visible against the colored background  
❌ **Don't:** Allow focus rings to blend into backgrounds, making keyboard navigation invisible
