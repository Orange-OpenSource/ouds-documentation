| Date | Number | Notes | Designer |
|------|--------|-------|----------|
| Apr 8, 2026 | - | • Documentation writing: Rich text | Anton Astafev |
| Mar 16, 2026 | - | • Documentation writing: | Maxime Tonnerre |
| | | ‎ ‎ ‎ • Mandatory field indication | |
| | | ‎ ‎ ‎ • Multiline and responsiveness | |
| | | ‎ ‎ ‎ • Technical layout adjustments | |
| Jan 6, 2026 | - | • Documentation writing: Definition update | Cyriaque Billard |
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