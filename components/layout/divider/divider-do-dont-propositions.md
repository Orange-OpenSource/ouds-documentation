# Divider — do & don't propositions

AI-generated propositions that no one has validated yet. They are not part of the documentation ([divider.md](divider.md)) and are not shown on zeroheight. Once a designer validates one, it moves into the full file.

## When to use

✅ To visually separate content without introducing strong hierarchy

✅ When you need to distinguish logical sections within the same screen or layout

✅ In lists, forms, or cards to improve readability and scannability

✅ When a heading or container would be semantically or visually excessive

## Orientation — do & don't

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

## Authorized colors — do & don't

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
