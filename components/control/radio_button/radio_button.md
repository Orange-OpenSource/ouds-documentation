# Guideline

## Intro 👈🤖

A radio button enables users to select exactly one option from a predefined set of mutually exclusive choices.

---

## Definition

A radio button is a user interface element that allows users to select a single option from a set of mutually exclusive choices, typically displayed as a circular input with a label that becomes filled when selected.

This component family is available in two variants:
• **Radio-button:** In this template, the component does not display any text or icon. This layout provides greater flexibility when creating other components that require a radio-button to be displayed.
• **Radio-button item:** In this template, the component displays multiple additional text elements and icon assets.

---

## Best for 👈🤔

✅ Single selection from a small set of 2–7 mutually exclusive options

✅ Settings or preferences where only one choice applies at a time

✅ Forms requiring explicit user commitment to one option

✅ Yes/No or binary choice questions on a page

✅ Filter controls where one category must be active

✅ Survey questions with predefined answer choices

✅ Configuration panels with exclusive mode selections

✅ Checkout flows for shipping or payment method selection

✅ User onboarding where one path must be chosen

✅ Legal or compliance forms requiring explicit single selection

---

## Anatomy 👈🤖

| # | Element | Purpose | Optional |
|---|---------|---------|----------|
| 1 | Radio indicator | Circular input showing selected/unselected state via fill or empty circle | N |
| 2 | Label | Primary text describing the selectable option | N |
| 3 | Extra label | Strong accompanying text providing additional emphasis for the label | Y |
| 4 | Description | Supporting text providing context or clarification for the option | Y |
| 5 | Icon | Visual element to enhance recognition or categorization of the option | Y |
| 6 | Error message | Text displayed when validation fails, explaining the error condition | Y |
| 7 | Divider | Horizontal line separating radio button items in a list | Y |
| 8 | Container (combined) | Interactive area encompassing indicator and label for click/tap targets; includes outlined variant for emphasis | N |

---

## Selected

Typically, a radio button has two main states: Selected and Unselected.

**`False`** The radio button is unselected. Used by default or when the user chooses another option in the group.

**`True`** The radio button is selected. Indicates the user's current active choice within the group.

---

## selected_do_&_dont 👈🤔

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

---

## Error

**`False`** The field is required but not selected. Example: the "I accept the terms" checkbox is not checked — user action is required.

**`True`** The field is selected but still invalid. Example: the user selects "Subscribe to newsletter" but doesn't provide an email — logical condition not met.

---

## error_do_&_dont 👈🤔

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

---

## Outlined

**`False`** This is the default layout of the component.

**`True`** Outlined radio buttons are designed to stand out and draw the user's attention. They are often used to emphasize significant or impactful options that require careful consideration in the interface.

---

## outlined_do_&_dont 👈🤔

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

---

## Reverse

**`False`** This is the default layout of the component. From left to right, the order of the elements is as follows: radio button / text / icon.

**`True`** As its name suggests, this layout is the reversed mirror of the "Default" template. From left to right, the order of the elements is as follows: icon / text / radio button. This variant is necessary for RTL mode and certain mobile use cases.

---

## reverse_do_&_dont 👈🤔

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

---

## Other boolean options

**`Extra label`** It is possible to display or hide strong accompanying text for the main label.

**`Description`** It is possible to display or hide accompanying text for the main label.

**`Icon`** It is possible to display or hide an icon. If displayed, this option includes functionality to choose any Solaris icon.

**`Divider`** It is possible to display or hide a dividing element (line).

**`Error message`** In the context where the component is in its "Error" true option, the error message can be displayed.

---

## other_boolean_options_do_&_dont 👈🤔

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

---

# Specs

## States

**`Enabled`** The default active state where the radio button is functional and selectable. It may show an unselected or selected style, with a label and helper text visible.

**`Hover`** When a user places a pointing device over a radio button, but has not yet taken action on it. This includes a subtle visual indicator (highlighted background or color change) to show interactivity.

**`Focus`** When a user selects a radio button via keyboard or voice command, but has not yet taken action on it. Mirrors the "Hover" state but includes an additional border.

**`Pressed`** An intermediate state that communicates a user has taken action on a radio button, and that it is in the process of navigating to a destination, triggering logic, or transmitting data.

**`Read only`** The radio button is displayed in a specific state (selected or unselected), but the user cannot modify it with a label and helper text visible.

**`Disabled`** The radio button is non-interactive and grayed out to indicate it cannot be selected or changed. The label and helper text are  muted.

**`Skeleton`** Improves the perceived loading time by providing a visual cue of where radio button will appear once fully loaded. Uses the "Skeleton" component, variant "Security marge=True".

---

## Layout and spacing

🚧 Content to be added

---

# Accessibility 👈🤖

## Accessibility intro

Radio buttons must meet WCAG 2.2 Level AA standards, ensuring keyboard operability, proper labeling, and clear state communication for all users including those using assistive technologies. For comprehensive accessibility guidance, see the [Orange Unified Design System Accessibility Overview](https://unified-design-system.orange.com/472794e18/p/88ebab-accessibility-and-sustainability).

---

## Accessibility Challenges

Radio buttons present unique accessibility challenges because they operate as groups where only one option can be selected, requiring proper grouping semantics, clear state indication, and coordinated keyboard navigation across multiple interactive elements.

### Key Challenges
- Communicating mutual exclusivity to screen reader users who cannot see visual relationships
- Managing roving tabindex for efficient keyboard navigation within groups
- Ensuring error states are announced and associated with the correct group
- Maintaining visible focus indicators across all interaction states

### Critical Success Factors
1. Group radio buttons using `<fieldset>` with `<legend>` or `role="radiogroup"` with `aria-labelledby` (WCAG 1.3.1)
2. Ensure each radio button has an accessible name via `<label>` or `aria-label` (WCAG 4.1.2)
3. Provide visible focus indicators with ≥3:1 contrast ratio (WCAG 2.4.7)
4. Associate error messages with the group using `aria-describedby` (WCAG 3.3.1)

---

## Design Requirements

### Structure & Labels
- [ ] **Group labeling**: Use `<fieldset>` and `<legend>` to provide group context ([Orange label guidelines](https://a11y-guidelines.orange.com/en/web/components-examples/))
- [ ] **Individual labels**: Every radio button has a visible `<label>` associated via `for`/`id`
- [ ] **Required indication**: Mark required groups with "(required)" in legend, use `aria-required="true"`

### Visual Design
- [ ] **Focus indicator**: 3:1 minimum contrast, visible on all backgrounds ([Focus guidelines](https://a11y-guidelines.orange.com/en/web/design/focus-visible/))
- [ ] **State contrast**: Selected/unselected states distinguishable without relying on color alone
- [ ] **Touch target**: Minimum 44×44px interactive area for radio button and label combined

### Content
- [ ] **Error messages**: ❌ "Error" / ✅ "Select your preferred contact method" ([Error guidelines](https://a11y-guidelines.orange.com/en/web/components-examples/forms/))
- [ ] **Concise labels**: Use clear, scannable option text under 3–4 words per label

---

## Testing Checklist

### Screen Reader Testing
- [ ] Test with NVDA (Windows), JAWS (Windows), VoiceOver (macOS/iOS), TalkBack (Android)
- [ ] Verify group label announced, option labels read, selected state communicated, error messages associated

### Keyboard Testing
- [ ] Tab moves focus to group, Arrow keys navigate between options, Space selects focused option
- [ ] Verify focus indicator visible with ≥3:1 contrast throughout all states

### Visual Testing
- [ ] Confirm selected/unselected states distinguishable by shape, not just color
- [ ] Verify error indicators include icon or text in addition to color change

Resources: [Orange Accessibility Testing Guide](https://a11y-guidelines.orange.com/en/web/toolbox/)

---

## Key WCAG Criteria

- **1.3.1 Info and Relationships** (A): Radio groups use proper `<fieldset>`/`<legend>` or ARIA grouping semantics
- **2.1.1 Keyboard** (A): All radio buttons operable via Tab and Arrow keys without mouse
- **2.4.7 Focus Visible** (AA): Visible focus indicator on active radio button with ≥3:1 contrast
- **3.3.1 Error Identification** (A): Errors identified in text and associated with radio group via `aria-describedby`
- **4.1.2 Name, Role, Value** (A): Radio button role, checked state, and accessible name exposed to assistive technology

For complete reference: [Orange Accessibility Guidelines - Form Components](https://a11y-guidelines.orange.com/en/web/components-examples/forms/)

---

## Additional Resources

- [Orange Accessibility Guidelines - Radio Buttons](https://a11y-guidelines.orange.com/en/web/components-examples/)
- [WCAG 2.2 Understanding 1.3.1 Info and Relationships](https://www.w3.org/WAI/WCAG22/Understanding/info-and-relationships)
- [WAI-ARIA Radio Group Pattern](https://www.w3.org/WAI/ARIA/apg/patterns/radio/)
- [Orange Design System - Accessibility & Sustainability](https://unified-design-system.orange.com/472794e18/p/88ebab-accessibility-and-sustainability)

---

# Changelog

| Date | Number | Notes | Designer |
|------|--------|-------|----------|
| Nov 7, 2025 | 1.4.0 | • A new Read-only variant has been added for the .Radiobutton.Indicator component, supporting two boolean variants — Selected = True/False. This variant introduces two new color tokens: | Anton Astafev |
| | | ‎ ‎ ‎ • ouds/color/action/read-only-primary — used for the indicator (shape) | |
| | | ‎ ‎ ‎ • ouds/color/action/read-only-secondary — used for the stroke | |
| | | • The new Read-only variant has been integrated into the Read-only variant of both the Radio button and Radio button Item components. | |
| | | • We replaced the token in Error text container ouds-control-text-input-space-padding-block-top-helper-text with ouds-control-control-item-space-padding-block-top-error-text. | |
| | | • "Helper text" is now called "Description". | |
| | | • "Additional label" is now called "Extra label". | |
| Oct 20, 2025 | 1.3.0 | • The Radio button item has been split into two boolean variants: → Error = True/False → Selected = True/False | Anton Astafev |
| | | • The divider color is now functional in the Error state — it changes dynamically according to the component status. | |
| | | • The icon in the Error state is fixed to .Component/alert/important; its color changes together with the divider depending on the component's status. → The new token $control-control-item-size-error-icon is used for the icon size. → The new token $control-text-input-space-padding-inline-error-icon is used for the error icon container. 🆕 Both tokens are now available in the latest release of the Token Library 2.1.0. | |
| | | • Added Error text (from the Input component) — it follows the same padding-inline as control-item (16px) and uses → $control-text-input-space-padding-block-top-helper-text for block padding. By default, the Error text adapts automatically to match the component status: → Selected → displays the corresponding default error message for the selected state. → Unselected → displays the corresponding default error message for the unselected state. | |
| | | • The "Read only" state has been updated to replace control items (in their disabled states) — both selected and unselected — with the Tag → Text only → Muted component: → Positive with label "Selected" if selected = True → Negative with label "Unselected" if selected = False | |
| | | • Harmonisation of spacing across the control-item family We've unified sizing tokens across the entire control-item family (previously they were defined per component) to align spacing with other control items such as Text input. Replacement note: instead of the single token padding inset 12, use the following tokens: → ouds/_control/control-item/space/padding-inline → 16 → ouds/_control/control-item/space/padding-block → 12 Additionally, for the control-item family: → ouds/_control/control-item/space/column-gap → 12 → ouds/_control/control-item/size/max-width → 480 | |
| Sep 19, 2025 | 1.2.0 | • In the initial settings, the 'Divider' variant is now hidden. | Maxime Tonnerre |
| Jul 21, 2025 | 1.1.0 | • The name of the family to which this component belongs is changing: Input → Control. As a result, the token naming convention is being updated. | Maxime Tonnerre |
| | | • Following the renaming of the 'Control' category, the name of the token sub-family 'control-item' is now becoming 'item'." | |
| Jan 22, 2025 | 1.0.0 | • Component creation | Maxime Tonnerre |