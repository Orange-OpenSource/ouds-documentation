## Definition

A Status Icon is a visual component used to communicate the functional state of a system or message, such as Success, Info, Warning, or Error. It provides quick, at-a-glance feedback using standardized colors and symbols to ensure consistent meaning across the product. A Status Icon is typically non-interactive and is used in contexts such as alerts, form validation, notifications, or system messages.

---

## Status

⚠️ Note:
Icons must never be replaced or customized. Each type has a dedicated, standardized icon that expresses its meaning clearly.

**`Positive`** Confirms that an action was completed successfully.
Uses a green color and the standard success icon.

**`Info`** Provides neutral information or updates about the system or account status. Uses blue for neutrality and clarity.

**`Warning`** Draws attention to potential issues or upcoming changes.
Uses yellow to signal caution while remaining non-blocking.

**`Negative`** Indicates a failure, error, or blocking issue that needs user attention.
Uses red color and must include the standardized error icon.

---

## Animated

**`True`** The Status Icon includes a subtle animation to reinforce the status change or draw attention to the state. The animation remains minimal and purposeful, supporting clarity without distraction.

**`False`** The Status Icon is displayed in a static state, without motion. It provides immediate visual feedback using color and symbol only.

---

## Multiline and responsiveness

**User zoom in/out**
The component's height and width must be flexible, never fixed, in order to automatically adapt its dimensions according to the level of zoom (the icons follow the same rules as the text).
In order to preserve the minimun interactive area during user zoom out, this component have a min-width and a min-height **of 28px**.
