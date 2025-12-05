# Guideline

## Intro

A checkbox allows users to select or deselect one or more options from a set independently.

---

## Definition

A checkbox component is a user interface element used to allow the user to selection-control or deselection-control an option. It is commonly used in forms, web interfaces, or applications to capture multiple or single choices.

This component family is available in two variants:
• **Checkbox:** In this template, the component does not display any text or icon. This layout provides greater flexibility when creating other components that require a checkbox to be displayed.
• **Checkbox item:** In this template, the component displays multiple additional text elements and icon assets.

---

## Best for

✅ Selecting multiple options from a list where choices are not mutually exclusive

✅ Accepting terms, conditions, or consent agreements requiring explicit user acknowledgment

✅ Filtering content in tables, lists, or search results

✅ Batch-selecting items for bulk actions like delete, move, or export

✅ Creating parent-child hierarchical selections with indeterminate state support

✅ Toggling feature settings that require form submission to take effect

✅ Collecting survey responses where multiple answers apply

✅ Enabling optional add-ons or features during checkout or configuration flows

✅ Building preference panels with independent on/off choices

✅ Confirming understanding of important information before proceeding

---

## Anatomy 👈🤖

| # | Element | Purpose | Optional |
|---|---------|---------|----------|
| 1 | Checkbox indicator | Visual control showing selected, unselected, or indeterminate state | N |
| 2 | Label | Text describing the option being selected | N |
| 3 | Description | Additional helper text providing context for the option | Y |
| 4 | Icon | Visual element supporting the label meaning | Y |
| 5 | Divider | Horizontal line separating checkbox items in a group | Y |
| 6 | Error icon | Alert indicator shown when validation fails | Y |
| 7 | Error message | Text explaining what went wrong and how to fix it | Y |

---

## Selection status

**`Selected`** Indicates that the user has selected the option.
This often corresponds to an action or validation.

**`Unselected`** By default, a checkbox is often in this state.
This state indicates that the user has not selected the associated option.

**`Indeterminate`** Often used when the checkbox represents a partial selection. For example, in a nested (hierarchical) list, a parent checkbox can be indeterminate if some but not all sub-options are checked.
This is not a state the user directly selects but is calculated by the system.

---

## selection_status_do_&_dont 👈🤔

✅ **Do:** Use indeterminate state only for parent-child hierarchies where some children are selected.
❌ **Don't:** Allow users to manually set a checkbox to indeterminate state—it should be system-calculated only.

✅ **Do:** Automatically update parent checkbox state when children change (all selected → checked, none → unchecked, some → indeterminate).
❌ **Don't:** Pre-select checkboxes by default as this increases the chance users will miss the question.

✅ **Do:** Use `aria-checked="mixed"` for indeterminate state to communicate status to assistive technologies.
❌ **Don't:** Treat indeterminate as a third value—it is presentational only and doesn't affect submitted data.

✅ **Do:** Order options logically—alphabetically, most-to-least common, or by workflow sequence.
❌ **Don't:** Confuse users by mixing checkboxes and radio buttons in the same option group.

✅ **Do:** Add hint text like "Select all that apply" to clarify multiple selections are allowed.
❌ **Don't:** Assume the visual difference between checkboxes and radios is obvious to all users.

---

## Error

**`False`** Used when the checkbox is unchecked but required.
Example: user must agree to terms, but didn't check the box.

**`True`** Used when the checkbox is checked but still invalid.
Example: the selection conflicts with another field or fails validation.

---

## error_do_&_dont 👈🤔

✅ **Do:** Validate checkbox selections on form submission, not when the user moves away from the field.
❌ **Don't:** Use inline validation on blur—wait until the user attempts to proceed.

✅ **Do:** Communicate errors through multiple channels—color, icon, and descriptive text message.
❌ **Don't:** Rely solely on color to indicate errors as this fails accessibility requirements.

✅ **Do:** Use `aria-describedby` to associate error messages with checkboxes for screen reader users.
❌ **Don't:** Disable the submit button when checkboxes are incomplete—show validation errors instead.

✅ **Do:** Provide specific, actionable error messages like "Select if you agree to the terms of service."
❌ **Don't:** Use vague messages like "This field is required" without explaining what action is needed.

✅ **Do:** Add visually hidden "Error:" prefix before error messages for screen reader announcement.
❌ **Don't:** Use native HTML5 validation—implement custom validation with `novalidate` on form elements.

---

## Reverse

**`False`** This is the default layout of the component.
From left to right, the order of the elements is as follows: checkbox / text / icon.

**`True`** As its name suggests, this layout is the reversed mirror of the "Default" template.
From left to right, the order of the elements is as follows: icon / text / checkbox. This variant is necessary for RTL mode and certain mobile use cases.

---

## reverse_do_&_dont 👈🤔

✅ **Do:** Position checkboxes to the left of labels in LTR contexts for easier scanning and discovery.
❌ **Don't:** Hardcode left/right positioning—use logical CSS properties that respond to text direction.

✅ **Do:** Use the reverse layout for RTL languages where checkbox should appear on the right side.
❌ **Don't:** Mix checkbox positions (left and right of label) within the same interface or form.

✅ **Do:** Test checkbox groups thoroughly in RTL mode to verify proper label alignment and reading order.
❌ **Don't:** Assume checkbox-to-label visual relationships will automatically reverse correctly.

✅ **Do:** Use logical properties like `marginStart` and `marginEnd` instead of physical `margin-left/right`.
❌ **Don't:** Forget to verify indeterminate and error states display correctly in reverse/RTL layout.

✅ **Do:** Consider mobile use cases where reverse layout may improve thumb reachability on large screens.
❌ **Don't:** Use reverse layout inconsistently—apply it systematically based on language direction or device context.

---

## Other boolean options

**`Description`** It is possible to display or hide accompanying text for the main label.

**`Icon`** It is possible to display or hide an icon. If displayed, this option includes functionality to choose any Solaris icon.

**`Divider`** It is possible to display or hide a dividing element (line).

**`Error message`** In the context where the component is in its "Error" true option, the error message can be displayed.

---

## other_boolean_options_do_&_dont 👈🤔

✅ **Do:** Use description text to explain accepted values or provide additional context for complex options.
❌ **Don't:** Include links within description text—screen readers may not announce them as interactive.

✅ **Do:** Keep descriptions to a single short sentence without full stops for scannability.
❌ **Don't:** Truncate checkbox labels with ellipsis—allow text to wrap to a second line instead.

✅ **Do:** Use dividers to create logical groupings or implement "none of the above" exclusive options.
❌ **Don't:** Overuse dividers—they should separate meaningful groups, not every individual option.

✅ **Do:** Use icons sparingly to reinforce label meaning when visual distinction adds genuine value.
❌ **Don't:** Add icons purely for decoration—they should serve a clear communicative purpose.

✅ **Do:** Display error messages immediately below the affected checkbox using consistent positioning.
❌ **Don't:** Hide error messages until form submission if real-time feedback would help users.

---

# Specs

## States

**`Enabled`** The status of the checkbox before a user has interacted with it, or other content affects it.

**`Hover`** When a user places a pointing device over a checkbox, but has not yet taken action on it.

**`Focus`** When a user selects a checkbox via keyboard or voice command, but has not yet taken action on it.
Mirrors the "Hover" state but includes an additional border.

**`Pressed`** An intermediate state that communicates a user has taken action on a checkbox, and that it is in the process of navigating to a destination, triggering logic, or transmitting data.

**`Read only`** The checkbox is displayed in a specific state (selected or unselected), but the user cannot modify it.

**`Disabled`** Used to indicate an option that cannot be selected.

**`Skeleton`** Improves the perceived loading time by providing a visual cue of where checkbox will appear once fully loaded.
Uses the "Skeleton" component, variant "Security marge=True".

---

## Layout and spacing

🚧 Content to be added

---

# Accessibility

## Accessibility intro

Checkbox components must meet WCAG 2.2 Level AA requirements for keyboard operability, visible focus indicators, and proper labeling. For comprehensive accessibility guidance, see the [Orange Unified Design System Accessibility Overview](https://unified-design-system.orange.com/472794e18/p/88ebab-accessibility-and-sustainability).

---

## Accessibility Challenges

Checkboxes present unique accessibility challenges due to their reliance on visual state indicators (checked, unchecked, indeterminate), the need for proper grouping semantics, and error state communication that must work across multiple modalities.

### Key Challenges

- Indeterminate state requires `aria-checked="mixed"` which some screen readers announce inconsistently
- Error states must be communicated through more than color alone
- Touch targets must be sufficiently large while maintaining visual design
- Grouped checkboxes require proper fieldset/legend structure for context

### Critical Success Factors

1. Use native `<input type="checkbox">` elements for maximum assistive technology compatibility
2. Associate labels programmatically using `for`/`id` attributes or wrapping structure
3. Implement visible focus indicators meeting 3:1 contrast ratio (WCAG 2.4.7)
4. Group related checkboxes with `<fieldset>` and `<legend>` elements

---

## Design Requirements

### Structure & Labels

- [ ] **Programmatic labels**: Every checkbox has an associated `<label>` element or `aria-label` ([Orange label guidelines](https://a11y-guidelines.orange.com/en/web/develop/textual-content/#provide-accessible-names))
- [ ] **Group structure**: Related checkboxes wrapped in `<fieldset>` with descriptive `<legend>`
- [ ] **Clickable area**: Both checkbox input and label text are clickable to increase target size

### Visual Design

- [ ] **Focus indicator**: Visible focus ring with ≥3:1 contrast ratio against background ([Orange focus guidelines](https://a11y-guidelines.orange.com/en/web/design/keyboard-navigation/#visible-focus))
- [ ] **Touch target**: Minimum 48×48dp touch target for mobile interactions
- [ ] **State differentiation**: Selected, unselected, and indeterminate states visually distinct without relying solely on color

### Content

- [ ] **Error communication**: ❌ Color only / ✅ Color + icon + text message ([Orange error guidelines](https://a11y-guidelines.orange.com/en/web/design/forms/#report-errors-accessibly))
- [ ] **Descriptive labels**: Labels clearly describe the option without requiring additional context

---

## Testing Checklist

### Screen Reader Testing

- [ ] Test with NVDA (Windows), JAWS (Windows), VoiceOver (macOS/iOS), TalkBack (Android)
- [ ] Verify: label announced, role "checkbox" stated, state communicated (checked/not checked/partially checked), error messages read

### Keyboard Testing

- [ ] Tab navigates to checkbox, Space toggles state, focus indicator visible with ≥3:1 contrast
- [ ] Verify disabled checkboxes are not focusable, read-only checkboxes remain in tab order

Resources: [Orange Accessibility Testing Guide](https://a11y-guidelines.orange.com/en/web/testing/)

---

## Key WCAG Criteria

- **1.3.1 Info and Relationships** (A): Checkbox groups use fieldset/legend; labels programmatically associated
- **2.1.1 Keyboard** (A): All checkbox functionality operable via keyboard without timing requirements
- **2.4.7 Focus Visible** (AA): Visible focus indicator with ≥3:1 contrast on all interactive states
- **3.3.1 Error Identification** (A): Errors identified in text and associated with checkboxes via `aria-describedby`
- **4.1.2 Name, Role, Value** (A): Native checkbox semantics communicate state changes; `aria-checked="mixed"` for indeterminate

For complete reference: [Orange Accessibility Guidelines - Forms](https://a11y-guidelines.orange.com/en/web/design/forms/)

---

## Additional Resources

- [Orange Accessibility Guidelines - Form Components](https://a11y-guidelines.orange.com/en/web/components-examples/)
- [WCAG 2.2 Understanding 4.1.2 Name, Role, Value](https://www.w3.org/WAI/WCAG22/Understanding/name-role-value.html)
- [Orange Design System - Accessibility & Sustainability](https://unified-design-system.orange.com/472794e18/p/88ebab-accessibility-and-sustainability)
- [WAI-ARIA Authoring Practices - Checkbox Pattern](https://www.w3.org/WAI/ARIA/apg/patterns/checkbox/)

---

# Changelog

| Date | Number | Notes | Designer |
|------|--------|-------|----------|
| Nov 7, 2025 | 2.4.0 | • A new Read-only variant has been added for the .Checkbox.Indicator component, supporting three states – Selected, Unselected, and Indeterminate. This variant introduces two new color tokens: • ouds/color/action/read-only-primary – used for the indicator (shape) • ouds/color/action/read-only-secondary – used for the stroke • The new Read-only variant has been integrated into the Read-only variant of both the Checkbox and Checkbox Itemcomponents. • We replaced the token in Error text container ouds-control-text-input-space-padding-block-top-helper-text with ouds-control-control-item-space-padding-block-top-error-text. • "Helper text" is now called "Description". | Anton Astafev |
| Oct 20, 2025 | 2.3.0 | • The "Selection status" variant has been restructured from six options (Selected / Selected error / Unselected / Unselected error / Indeterminate / Indeterminate error) into three base variants: → Selected → Unselected → Indeterminate • Each variant now includes a boolean property to control the Error state (Error = True/False). • The divider color is now functional in the Error state – it changes dynamically according to the component status. • The icon in the Error state is fixed to .Component/alert/important; its color changes together with the divider depending on the component's status. → The new token $control-control-item-size-error-icon is used for the icon size. → The new token $control-text-input-space-padding-inline-error-icon is used for the error icon container. 🆕 Both tokens are now available in the latest release of the Token Library 2.1.0. • Added Error text (from the Input component) – it follows the same padding-inline as control-item (16px) and uses → $control-text-input-space-padding-block-top-helper-text for block padding. By default, the Error text adapts automatically to match the component status: → Selected → displays the corresponding default error message for the selected state. → Unselected → displays the corresponding default error message for the unselected state. → Indeterminate → displays the corresponding default error message for the indeterminate state. • The "Read only" state has been updated to replace disabled control items with the Tag → Text only → Mutedcomponent: → Positive with label "Selected" → Negative with label "Unselected" → Caution with label "Indeterminate" • Harmonisation of spacing across the control-item family We've unified sizing tokens across the entire control-item family (previously they were defined per component) to align spacing with other control items such as Text input. Replacement note: instead of the single token padding inset 12, use the following tokens: → ouds/_control/control-item/space/padding-inline → 16 → ouds/_control/control-item/space/padding-block → 12 Additionally, for the control-item family: → ouds/_control/control-item/space/column-gap → 12 → ouds/_control/control-item/size/max-width → 480 | Anton Astafev |
| Sep 19, 2025 | 2.2.0 | • In the initial settings, the 'Divider' variant is now hidden. | Maxime Tonnerre |
| Jul 21, 2025 | 2.1.0 | • The name of the family to which this component belongs is changing: Input → Control. As a result, the token naming convention is being updated. • Following the renaming of the 'Control' category, the name of the token sub-family 'control-item' is now becoming 'item'." | Maxime Tonnerre |
| Fev 13, 2025 | 2.0.0 | • Restructuring the component to optimize its factoring. • Creation of the nested component ".CheckboxItem.Control." • The component is now divided into two distinct components: • Checkbox • Checkbox item | Maxime Tonnerre |
| Jan 17, 2025 | 1.0.0 | • Component creation | Maxime Tonnerre |