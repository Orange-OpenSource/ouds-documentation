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