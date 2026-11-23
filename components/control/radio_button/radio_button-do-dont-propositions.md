# Radio button — do & don't propositions

AI-generated propositions that no one has validated yet. They are not part of the documentation ([radio_button.md](radio_button.md)) and are not shown on zeroheight. Once a designer validates one, it moves into the full file.

## When to use

✅ When users must select exactly one option from a predefined set

✅ When all options should be visible and comparable at the same time

✅ For choices that are mutually exclusive and require clarity over flexibility

✅ When the selection takes effect immediately or clearly defines the next step

## Selected — do & don't

✅ **Do:** Pre-select a default option when a recommended or most common choice exists to reduce user effort  
❌ **Don't:** Pre-select an option that could commit users to unwanted actions like subscriptions or agreements

✅ **Do:** Ensure the selected state is visually distinct with a filled indicator and sufficient color contrast  
❌ **Don't:** Use subtle visual differences that make it difficult to distinguish selected from unselected states

✅ **Do:** Allow users to change their selection freely before form submission  
❌ **Don't:** Lock selections or require page refresh to change a radio button choice

✅ **Do:** Provide a "None" or "Not applicable" option if no selection should be a valid user choice  
❌ **Don't:** Force users to select an option when the question may not apply to them

✅ **Do:** Automatically deselect the previous option when a new one is selected within the group  
❌ **Don't:** Allow multiple radio buttons in the same group to be selected simultaneously

## Error — do & don't

✅ **Do:** Display error messages directly below the radio group with clear, actionable language like "Select an option"  
❌ **Don't:** Use generic error messages like "Invalid input" that don't explain what action is required

✅ **Do:** Use a distinct error color (typically red) for the indicator border and error message text  
❌ **Don't:** Rely solely on color to indicate errors—include text and icons for accessibility

✅ **Do:** Associate error messages programmatically with the radio group using `aria-describedby`  
❌ **Don't:** Place error messages far from the radio group where users may miss the connection

✅ **Do:** Clear error states immediately when the user makes a valid selection  
❌ **Don't:** Keep error indicators visible after the user has corrected the issue

✅ **Do:** Validate on blur or form submission rather than on every interaction to avoid premature errors  
❌ **Don't:** Show error states before the user has had a chance to interact with the radio group

## Outlined — do & don't

✅ **Do:** Use outlined variants sparingly for high-importance decisions like pricing plans or subscription tiers  
❌ **Don't:** Apply outlined styling to every radio group, which diminishes its emphasis effect

✅ **Do:** Maintain consistent padding and border styling across all outlined radio buttons in a group  
❌ **Don't:** Mix outlined and non-outlined radio buttons within the same selection group

✅ **Do:** Ensure outlined borders have sufficient contrast against the background (minimum 3:1 ratio)  
❌ **Don't:** Use light gray borders on white backgrounds that fail accessibility contrast requirements

✅ **Do:** Increase touch target size when using outlined variants to accommodate the larger visual footprint  
❌ **Don't:** Reduce clickable areas to match only the visible border boundaries

✅ **Do:** Use outlined variants when radio options contain rich content like descriptions or icons  
❌ **Don't:** Use outlined variants for simple binary choices where standard radio buttons suffice

## Reverse — do & don't

✅ **Do:** Use reverse layout for right-to-left (RTL) languages like Arabic and Hebrew  
❌ **Don't:** Use reverse layout arbitrarily without considering reading direction conventions

✅ **Do:** Apply reverse layout consistently across all radio buttons when supporting RTL interfaces  
❌ **Don't:** Mix LTR and RTL radio button layouts on the same page or within the same form

✅ **Do:** Position the radio indicator on the trailing edge (right side for LTR, left for RTL) for mobile list interfaces  
❌ **Don't:** Place indicators in inconsistent positions across different screen sizes

✅ **Do:** Ensure tab order and focus management work correctly regardless of visual layout direction  
❌ **Don't:** Assume visual order equals DOM order—verify keyboard navigation flows logically

✅ **Do:** Test reverse layouts with screen readers to confirm proper announcement order  
❌ **Don't:** Rely solely on visual testing when implementing layout variants

## Other boolean options — do & don't

✅ **Do:** Use descriptions to provide helpful context that aids decision-making between options  
❌ **Don't:** Add descriptions to every radio button when options are already self-explanatory

✅ **Do:** Use icons that clearly represent the option and are recognizable at small sizes  
❌ **Don't:** Use decorative icons that don't add meaningful information to the selection

✅ **Do:** Use dividers to create visual separation in long lists of radio button items  
❌ **Don't:** Add dividers to groups with only 2–3 options where separation isn't needed

✅ **Do:** Keep extra labels concise and complementary to the main label text  
❌ **Don't:** Duplicate information between the main label and extra label

✅ **Do:** Show error messages only when validation has failed and hide them upon correction  
❌ **Don't:** Display placeholder error message space when no error exists
