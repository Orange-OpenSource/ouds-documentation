# Guideline

## Intro 👈🤖

A switch is a binary control that allows users to toggle settings on or off with immediate effect.

---

## Definition

A switch is a component that allows the user to toggle between two states, typically "on" and "off." It is often represented as a button or a slider that changes position or color to indicate the current state. Switches are used to enable or disable features, options, or settings in an intuitive and visual manner.

This component family is available in two variants:
• **Switch:** In this template, the component does not display any text or icon. This layout provides greater flexibility when creating other components that require a switch to be displayed.
• **Switch item:** In this template, the component displays multiple additional text elements and icon assets.

---

## Best for 👈🤔

✅ Enabling or disabling system settings that take effect immediately

✅ Toggling application features on or off without additional confirmation

✅ Controlling persistent binary states like dark mode or notifications

✅ Settings pages where users expect instant feedback upon interaction

✅ Mobile-first interfaces where tap-to-toggle is the expected behavior

✅ Preferences that can be quickly reversed without consequences

✅ Standalone options that don't require form submission

✅ Wi-Fi, Bluetooth, or connectivity controls with immediate activation

✅ Enabling or disabling auto-save, auto-update, or background sync features

✅ Privacy settings such as "Share my location" or "Allow analytics"

---

## Anatomy 👈🤖

| # | Element | Purpose | Optional |
|---|---------|---------|----------|
| 1 | Track | The horizontal rail where the cursor slides, indicating the toggle path | N |
| 2 | Cursor (Thumb) | The circular element that moves between on/off positions to show current state | N |
| 3 | Selected icon | Checkmark icon displayed on cursor when switch is in the "on" state | Y |
| 4 | Label | Text describing the setting or feature being controlled | Y |
| 5 | Description | Supporting text providing additional context below the label | Y |
| 6 | Icon | Visual indicator that helps identify the setting category | Y |
| 7 | Divider | Horizontal line separating switch items in a list | Y |
| 8 | Error message | Text displayed when the switch state causes a validation error | Y |

---

## State

**`Enabled`** The status of the switch before a user has interacted with it, or other content affects it.

**`Hover`** When a user places a pointing device over a switch, but has not yet taken action on it.

**`Focus`** When a user selects a switch via keyboard or voice command, but has not yet taken action on it. Mirrors the "Hover" state but includes an additional border.

**`Pressed`** An intermediate state that communicates a user has taken action on a switch, and that it is in the process of navigating to a destination, triggering logic, or transmitting data.

**`Read only`** The switch is displayed in a specific state (true or false), but the user cannot modify it.

**`Disabled`** Used to indicate an option that cannot be selected.

**`Skeleton`** Improves the perceived loading time by providing a visual cue of where switch will appear once fully loaded. Uses the "Skeleton" component, variant "Security marge=True".

## state_do_&_dont 👈🤔

✅ **Do:** Use the disabled state only when the switch will become available based on another condition or user action.  
❌ **Don't:** Disable switches without providing context about why or how to enable them.

✅ **Do:** Ensure the focus state has a visible indicator with at least 3:1 contrast ratio against adjacent colors.  
❌ **Don't:** Remove the default focus outline without providing an equally prominent custom indicator.

✅ **Do:** Use skeleton states during initial page load to indicate where interactive content will appear.  
❌ **Don't:** Display skeleton states for more than a few seconds as users may perceive this as broken functionality.

✅ **Do:** Make the read-only state visually distinct from disabled to communicate that the value is intentionally locked.  
❌ **Don't:** Use read-only when disabled would be more appropriate—read-only implies the value is meaningful and intentional.

✅ **Do:** Provide visual feedback during the pressed state to confirm the user's action was registered.  
❌ **Don't:** Allow the pressed state to persist longer than necessary as it may confuse users about the actual toggle state.

---

## Selected

Typically, a switch has two main states: Selected and Unselected.

**`False`** The switch is off — the option or feature is disabled. Used as the default state before activation.

**`True`** The switch is on — the option or feature is enabled. Indicates that the setting or action is currently active.

## selected_do_&_dont 👈🤔

✅ **Do:** Use distinct visual cues (color, position, icon) to clearly differentiate between on and off states.  
❌ **Don't:** Rely solely on color to indicate the selected state—users with color blindness may not perceive the difference.

✅ **Do:** Position the cursor to the right of the track for "on" and left for "off" to match user expectations.  
❌ **Don't:** Invert the cursor position convention as this creates confusion about which state is active.

✅ **Do:** Apply the action immediately when the user toggles the switch without requiring a separate save action.  
❌ **Don't:** Use switches for actions that require confirmation or have significant consequences.

✅ **Do:** Display a checkmark icon inside the cursor when selected to reinforce the active state visually.  
❌ **Don't:** Add animation that delays the visual feedback of state change beyond 200ms.

✅ **Do:** Ensure the default state (usually off) makes sense for first-time users and respects privacy.  
❌ **Don't:** Pre-select switches in ways that may trick users into enabling unwanted features.

---

## Error

**`False`** The switch is unselected or turned off, but this value is invalid. Used when a required action hasn't been completed or an active state is expected.

**`True`** The switch holds a value, but it does not meet logical or validation requirements. Used when the current state (on or off) causes a conflict or violates form rules.

## error_do_&_dont 👈🤔

✅ **Do:** Display error messages directly below the switch with clear, actionable text explaining how to resolve the issue.  
❌ **Don't:** Use generic error messages like "Invalid selection" without specifying what the user should do.

✅ **Do:** Use a distinct error color (typically red) for the divider and icon to draw attention to the validation issue.  
❌ **Don't:** Rely solely on color to indicate errors—include an icon and text for accessibility.

✅ **Do:** Provide different error messages for selected and unselected states when the context requires clarification.  
❌ **Don't:** Show the same error message regardless of the switch state if the required action differs.

✅ **Do:** Associate error messages with the switch using `aria-describedby` for screen reader accessibility.  
❌ **Don't:** Position error messages far from the switch where users may not notice them.

✅ **Do:** Clear the error state immediately when the user corrects the issue by toggling the switch.  
❌ **Don't:** Require users to perform additional actions (like clicking a "validate" button) to clear error states.

---

## Reverse

**`False`** This is the default layout of the component. From left to right, the order of the elements is as follows: icon / text / switch.

**`True`** As its name suggests, this layout is the reversed mirror of the "Default" template. From left to right, the order of the elements is as follows: switch / text / icon. This variant is necessary for RTL mode and certain mobile use cases.

## reverse_do_&_dont 👈🤔

✅ **Do:** Use the reverse layout consistently throughout RTL (right-to-left) language interfaces.  
❌ **Don't:** Mix default and reverse layouts inconsistently within the same screen or context.

✅ **Do:** Apply the reverse layout when the switch control needs to be the primary visual anchor on the left.  
❌ **Don't:** Use reverse layout arbitrarily—always have a clear UX rationale for the choice.

✅ **Do:** Maintain the same touch target size and spacing in both default and reverse layouts.  
❌ **Don't:** Reduce interactive area when switching layouts as this affects accessibility.

✅ **Do:** Test both layouts with screen readers to ensure announcement order remains logical.  
❌ **Don't:** Assume visual order matches reading order—verify with assistive technologies.

✅ **Do:** Use reverse layout on mobile when the switch is the primary action and needs immediate thumb access.  
❌ **Don't:** Switch between layouts based on screen size without considering consistency.

---

## Other boolean options

**`Description`** It is possible to display or hide accompanying text for the main label.

**`Icon`** It is possible to display or hide an icon. If displayed, this option includes functionality to choose any Solaris icon.

**`Divider`** It is possible to display or hide a dividing element (line).

**`Error message`** In the context where the component is in its "Error" true option, the error message can be displayed.

## other_boolean_options_do_&_dont 👈🤔

✅ **Do:** Include description text when the label alone doesn't provide enough context for users to make informed decisions.  
❌ **Don't:** Add description text that merely repeats the label or provides no additional value.

✅ **Do:** Use icons that clearly represent the category or type of setting being controlled.  
❌ **Don't:** Use decorative icons that don't add meaning or could be confused with interactive elements.

✅ **Do:** Use dividers to visually group related switch items and improve scanability in long lists.  
❌ **Don't:** Add dividers between every switch item when they create visual noise without aiding comprehension.

✅ **Do:** Display error messages only when the switch state genuinely conflicts with system or form requirements.  
❌ **Don't:** Show error messages for optional switches that have valid states in both on and off positions.

✅ **Do:** Keep description text concise—ideally one line—to maintain visual hierarchy.  
❌ **Don't:** Use description text as a substitute for proper documentation or help content.

---

# Specs

## States

**`Enabled`** The status of the switch before a user has interacted with it, or other content affects it.

**`Hover`** When a user places a pointing device over a switch, but has not yet taken action on it.

**`Focus`** When a user selects a switch via keyboard or voice command, but has not yet taken action on it. Mirrors the "Hover" state but includes an additional border.

**`Pressed`** An intermediate state that communicates a user has taken action on a switch, and that it is in the process of navigating to a destination, triggering logic, or transmitting data.

**`Read only`** The switch is displayed in a specific state (true or false), but the user cannot modify it.

**`Disabled`** Used to indicate an option that cannot be selected.

**`Skeleton`** Improves the perceived loading time by providing a visual cue of where switch will appear once fully loaded. Uses the "Skeleton" component, variant "Security marge=True".

---

## Layout and spacing

🚧 Content to be added

---

# Accessibility 👈🤖

## Accessibility intro

Switch components must meet WCAG 2.2 Level AA standards to ensure all users can operate toggle controls regardless of ability. For comprehensive accessibility guidance, see the [Orange Unified Design System Accessibility Overview](https://unified-design-system.orange.com/472794e18/p/88ebab-accessibility-and-sustainability).

---

## Accessibility Challenges

Switches present unique accessibility challenges because they communicate binary state changes that must be perceivable, operable, and understandable across all input methods and assistive technologies. The visual metaphor of a physical switch doesn't translate directly to non-visual contexts.

### Key Challenges
- Communicating current state (on/off) clearly to screen reader users without visual cues
- Ensuring immediate state changes are announced without disrupting user workflow
- Maintaining consistency between visual appearance and programmatic state
- Supporting both touch and keyboard interaction with adequate target sizes

### Critical Success Factors
1. Use `role="switch"` with `aria-checked` to properly convey on/off semantics (WCAG 4.1.2)
2. Provide visible focus indicators meeting 3:1 contrast ratio (WCAG 2.4.7)
3. Ensure label text clearly describes what the switch controls (WCAG 3.3.2)
4. Associate error messages programmatically using `aria-describedby` (WCAG 3.3.1)

---

## Design Requirements

### Structure & Labels
- [ ] **Programmatic label**: Associate visible label with switch using `for`/`id` or `aria-labelledby` ([Orange Forms Guide](https://a11y-guidelines.orange.com/en/web/develop/forms/))
- [ ] **Role and state**: Use `role="switch"` with `aria-checked="true|false"` to communicate state
- [ ] **Error association**: Link error messages via `aria-describedby` when in error state

### Visual Design
- [ ] **Focus indicator**: Visible focus ring with ≥3:1 contrast ratio ([Focus Guidelines](https://a11y-guidelines.orange.com/en/web/design/colors-and-contrasts/#make-sure-there-is-enough-contrast-between-the-colors))
- [ ] **State differentiation**: Use position, color, AND icon to indicate on/off (not color alone)
- [ ] **Touch target**: Minimum 48×48px interactive area for touch accessibility

### Content
- [ ] **Clear labels**: ❌ "Enable" / ✅ "Enable notifications for new messages"
- [ ] **Actionable errors**: Error text must explain how to resolve the issue

---

## Testing Checklist

### Screen Reader Testing
- [ ] Test with NVDA (Windows), VoiceOver (macOS/iOS), TalkBack (Android)
- [ ] Verify: role announced as "switch", state as "on/off", label read correctly, errors associated

### Keyboard Testing
- [ ] Tab navigates to switch, Space/Enter toggles state, focus indicator visible (≥3:1 contrast)
- [ ] Verify disabled switches are skipped in tab order, read-only switches are focusable but not editable

Resources: [Orange Keyboard Navigation Guide](https://a11y-guidelines.orange.com/en/web/toolbox/methods-and-test-tools/keyboard-navigation/)

---

## Key WCAG Criteria

- **2.1.1 Keyboard** (A): Switch must be operable via keyboard using Space or Enter keys
- **2.4.7 Focus Visible** (AA): Visible focus indicator with ≥3:1 contrast when switch receives focus
- **3.3.1 Error Identification** (A): Errors identified in text and associated via `aria-describedby`
- **3.3.2 Labels or Instructions** (A): Visible label provided that clearly describes the switch purpose
- **4.1.2 Name, Role, Value** (A): Use `role="switch"` and `aria-checked` to communicate state to AT

For complete reference: [Orange Accessibility Guidelines - Components](https://a11y-guidelines.orange.com/en/web/components-examples/)

---

## Additional Resources

- [W3C WAI-ARIA Switch Pattern](https://www.w3.org/WAI/ARIA/apg/patterns/switch/)
- [Orange Accessibility Guidelines - Forms](https://a11y-guidelines.orange.com/en/web/develop/forms/)
- [MDN ARIA: switch role](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Roles/switch_role)
- [Orange Design System - Accessibility & Sustainability](https://unified-design-system.orange.com/472794e18/p/88ebab-accessibility-and-sustainability)

---

# Changelog

| Date | Number | Notes | Designer |
|------|--------|-------|----------|
| Nov 7, 2025 | 1.5.0 | • A new Read-only variant has been added for the .Switch.Indicator component, supporting two boolean variants — Selected = True/False. This variant introduces two new color tokens: | Anton Astafev |
| | | ‎ ‎ ‎ ‎ • ouds/color/action/read-only-primary | |
| | | ‎ ‎ ‎ ‎ • ouds/color/action/read-only-secondary | |
| | | • The new Read-only variant has been integrated into the Read-only variant of both the Switch and Switch Item components. | |
| | | • We replaced the token in Error text container ouds-control-text-input-space-padding-block-top-helper-text with ouds-control-control-item-space-padding-block-top-error-text. | |
| | | • "Helper text" is now called "Description". | |
| Oct 20, 2025 | 1.4.0 | • The Switch item has been split into two boolean variants: → Error = True/False → Selected = True/False | Anton Astafev |
| | | • The divider color is now functional in the Error state — it changes dynamically according to the component status. | |
| | | • The icon in the Error state is fixed to .Component/alert/important; its color changes together with the divider depending on the component's status. → The new token $control-control-item-size-error-icon is used for the icon size. → The new token $control-text-input-space-padding-inline-error-icon is used for the error icon container. 🆕 Both tokens are now available in the latest release of the Token Library 2.1.0. | |
| | | • Added Error text (from the Input component) — it follows the same padding-inline as control-item (16px) and uses → $control-text-input-space-padding-block-top-helper-text for block padding. By default, the Error text adapts automatically to match the component status: → Selected → displays the corresponding default error message for the selected state. → Unselected → displays the corresponding default error message for the unselected state. | |
| | | • The "Read only" state will be updated with the goal of replacing the control items (in their "disabled" states), whether selected or unselected, with the component Tag → Text only → Muted: → Positive with a label text "Selected" if status selected=True → Negative with a label text "Unselected" if status selected=False | |
| | | • Harmonisation of spacing across the control-item family We've unified sizing tokens across the entire control-item family (previously they were defined per component) to align spacing with other control items such as Text input. Replacement note: instead of the single token padding inset 12, use the following tokens: → ouds/_control/control-item/space/padding-inline → 16 → ouds/_control/control-item/space/padding-block → 12 Additionally, for the control-item family: → ouds/_control/control-item/space/column-gap → 12 → ouds/_control/control-item/size/max-width → 480 | |
| Sep 19, 2025 | 1.3.0 | • In the initial settings, the 'Divider' variant is now hidden. | Maxime Tonnerre |
| Jul 21, 2025 | 1.2.0 | • The name of the family to which this component belongs is changing: Input → Control. As a result, the token naming convention is being updated. | Maxime Tonnerre |
| | | • Following the renaming of the 'Control' category, the name of the token sub-family 'control-item' is now becoming 'item'." | |
| Jun 16, 2025 | 1.1.0 | • Modification of the minimum height of the frame containing the component "Switch" to increase the interactive area (48px). Component token: $ouds-input-switch-size-min-height-interactive-area | Maxime Tonnerre |
| | | • Application of a border radius token to the "Focus" and "Focus inset" frames. The UI rendering of the focus state stroke of the component is now rounded like the rest of the component. Component token: $ouds-input-switch-border-radius-track | |
| | | • Application of a border radius token to the "Content" frame. The UI rendering of the skeleton state stroke of the component is now rounded like the rest of the component. Component token: $ouds-input-switch-border-radius-track | |
| Mar 6, 2025 | 1.0.0 | • Component creation | Jérôme Regnier |