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

# Accessibility

## Motion & Animation accessibility rules

In terms of animation, there are accessibility criteria to consider: “Animation from Interactions” and “Pause, Stop, Hide.”
These two main criteria address different issues:

**Pause, Stop, Hide - WCAG 2.2.2**
This concerns moving, blinking, scrolling, or automatically updating content.
The question to ask is: does the animation start automatically and meet the criterion’s conditions?
When a relevant animation lasts more than 5 seconds, users must be able to pause, stop, or hide it.
The two criteria should therefore be evaluated independently.

**Reduced Motion (Animation from Interactions) - WCAG 2.3.3**
This primarily concerns motion-based animations triggered by user interaction.
The question to ask is: is the movement essential to the functionality or to the information being conveyed?
If not, the animation should be removed, reduced, or replaced when the user has enabled Reduced Motion.

ℹ️ The reduced motion preference can be configured by the user at the operating system level and is available to websites through the CSS prefers-reduced-motion media feature.

Concrete application to the Switch:

**Pause, Stop, Hide**
The animation of a switch is triggered by a user action and therefore does not generally fall within the scope of this criterion.
If the state change triggers additional animation or automatically moving content that meets the conditions of the criterion, that content must be evaluated separately.

**Reduced Motion**
The animation applied when a switch changes state is generally not essential to its functionality or to understanding its state.
When Reduced Motion is enabled, the animation should therefore be removed or replaced with an instantaneous transition.
The state of the switch must remain clearly identifiable without relying on animation.
Default: animated state change
Reduced Motion: instantaneous state change

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