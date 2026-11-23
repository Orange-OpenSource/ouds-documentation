# Filter chip expand — do & don't propositions

AI-generated propositions that no one has validated yet. They are not part of the documentation ([filter_chip_expand.md](filter_chip_expand.md)) and are not shown on zeroheight. Once a designer validates one, it moves into the full file.

## When to use

✅ When a filter has multiple, dynamic, or changing values

✅ To keep the interface compact while still allowing detailed filter selection

✅ For filters that require a dropdown or secondary choice to define their value

✅ When filter configuration should stay close to the results, not in a separate panel

## Selection Status — do & don't

✅ **Do:** Use a prominent visual change like border color or weight to distinguish selected from unselected states  
❌ **Don't:** Rely solely on color to communicate selection status without additional indicators

✅ **Do:** Display a checkmark or tick icon alongside the label to reinforce the selected state  
❌ **Don't:** Use ambiguous icons that could be confused with other actions like delete or close

✅ **Do:** Include a counter badge when multiple options are selected within one filter category  
❌ **Don't:** Show counters for single-select filters where only one option can be active

✅ **Do:** Ensure selected chips are immediately distinguishable at a glance in filter groups  
❌ **Don't:** Make the visual difference so subtle that users miss which filters are currently applied

✅ **Do:** Allow users to quickly clear selections by interacting with the chip or a dedicated clear action  
❌ **Don't:** Force users to re-open the dropdown and manually deselect each option individually

## Expanded — do & don't

✅ **Do:** Position the dropdown directly below or adjacent to the chip maintaining visual connection  
❌ **Don't:** Display the dropdown far from the chip causing users to lose context of which filter they're editing

✅ **Do:** Use the chevron icon direction to clearly indicate expanded (up) versus collapsed (down) state  
❌ **Don't:** Use the same chevron direction for both states or omit the directional indicator entirely

✅ **Do:** Keep the dropdown open while users make multiple selections in multiselect scenarios  
❌ **Don't:** Close the dropdown after each selection forcing users to repeatedly reopen it

✅ **Do:** Allow closing the dropdown via clicking outside, pressing Escape, or clicking the chip again  
❌ **Don't:** Require a specific close button as the only way to dismiss the dropdown

✅ **Do:** Maintain focus management so keyboard users can navigate between chip and dropdown seamlessly  
❌ **Don't:** Trap focus in the dropdown or lose focus position when the dropdown closes
