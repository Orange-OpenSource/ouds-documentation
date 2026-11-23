# Breadcrumb — do & don't propositions

AI-generated propositions that no one has validated yet. They are not part of the documentation ([breadcrumb.md](breadcrumb.md)) and are not shown on zeroheight. Once a designer validates one, it moves into the full file.

## When to use

✅ You need to show the user’s current location within a page or product hierarchy

✅ The interface has multiple levels of navigation (2+ levels)

✅ Users may want to quickly navigate back to higher-level pages

✅ The structure is complex and a page title alone is not enough for orientation

## Drilldown — do & don't

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
