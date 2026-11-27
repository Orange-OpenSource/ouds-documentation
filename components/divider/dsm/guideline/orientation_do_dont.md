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