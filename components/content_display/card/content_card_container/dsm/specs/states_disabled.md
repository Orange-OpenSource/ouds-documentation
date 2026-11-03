**`Disabled`** The card and its contents communicate an unavailable state. All interactive elements within the slot must also be disabled and must not respond to user interaction.

In Figma, changing the card state does not automatically update slotted content.

⚠️ Designers must manually set nested interactive components to their Disabled state and replace content color tokens, for example content/default with content/disabled, wherever applicable.

⚠️ Do not apply a global opacity reduction to the entire slot content.  
Text and nested interactive components must use their corresponding Disabled states or color tokens. Images and illustrations must use the predefined OUDS disabled opacity token, which corresponds to 20% opacity in the current specification.
