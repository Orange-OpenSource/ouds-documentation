# Filter chip — do & don't propositions

AI-generated propositions that no one has validated yet. They are not part of the documentation ([filter_chip.md](filter_chip.md)) and are not shown on zeroheight. Once a designer validates one, it moves into the full file.

## When to use

✅ To let users apply or remove filters quickly without leaving the current context

✅ When multiple filters can be combined and toggled independently

✅ For refining lists, search results, or collections in a lightweight, visible way

✅ When filters represent an active, persistent state in the UI

## Selected — do & don't

✅ **Do:** Use a clear visual indicator like a checkmark or filled background to show selected state  
❌ **Don't:** Rely solely on subtle color changes that may not be perceivable by all users

✅ **Do:** Maintain consistent selected styling across all filter chips in a group  
❌ **Don't:** Mix different selection indicator styles within the same filter set

✅ **Do:** Ensure selected chips have sufficient color contrast (4.5:1 minimum) against the background  
❌ **Don't:** Use colors that only differ in hue without adequate luminance contrast

✅ **Do:** Provide immediate visual feedback when a chip transitions between selected and unselected states  
❌ **Don't:** Delay selection feedback or require additional confirmation for simple filter toggles

✅ **Do:** Consider pre-selecting sensible defaults when appropriate to reduce user effort  
❌ **Don't:** Pre-select all filters as this defeats the purpose of filtering content

## Layouts — do & don't

✅ **Do:** Use text-only layouts when filter labels are self-explanatory and space is available  
❌ **Don't:** Force icon-only layouts when the meaning isn't universally understood

✅ **Do:** Combine text with icons when visual reinforcement improves scannability  
❌ **Don't:** Add decorative icons that don't contribute to comprehension

✅ **Do:** Reserve icon-only layouts for universally recognized symbols like favorites or status indicators  
❌ **Don't:** Use ambiguous or custom icons without text labels in icon-only mode

✅ **Do:** Keep text labels concise—ideally one to two words maximum  
❌ **Don't:** Include verbs like "Select" or "Filter" within chip labels

✅ **Do:** Maintain consistent layout type within a single filter group  
❌ **Don't:** Mix text-only and icon-only chips arbitrarily within the same filter set
