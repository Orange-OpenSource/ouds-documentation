**`Enabled`** The card displays its content normally. Interactive elements within the slot remain independently accessible and retain their own
interaction states.

The card can be displayed on different predefined OUDS background surfaces according to its layout context. The background context must remain consistent when switching between card states. Interactive elements placed within the slot retain their own states independently of the container.

**`Disabled`** The card and its contents communicate an unavailable state. All interactive elements within the slot must also be disabled and must not respond to user interaction.

In Figma, changing the card state does not automatically update slotted content.

⚠️ Designers must manually set nested interactive components to their Disabled state and replace content color tokens, for example content/default with content/disabled, wherever applicable.

⚠️ Do not apply a global opacity reduction to the entire slot content.  
Text and nested interactive components must use their corresponding Disabled states or color tokens. Images and illustrations must use the predefined OUDS disabled opacity token, which corresponds to 20% opacity in the current specification.

**`Skeleton`** The Skeleton state represents content that has not yet loaded. Replace the final content with non-interactive placeholders that reflect the card’s expected layout and visual hierarchy.

During the Skeleton state, the card must display non-interactive placeholders only. Interactive controls within the slot must not be accessible or actionable until the actual content has finished loading.