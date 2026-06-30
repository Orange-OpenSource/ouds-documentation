## Definition

An inline alert is a lightweight UI element integrated into the content flow. It conveys information, system feedback, and status changes through short, prominent, persistent, and non-actionable messages. The inline alert includes a functional icon and a semantic colour, but does not have a close button or an action link. The inline alert remains visible and does not disappear.

---

## State

**`Enabled`** Displayed when the inline alert is active and content is available. Shows an icon and short text message to provide immediate, contextual feedback within the interface.

**`Skeleton`** Used as a placeholder while the alert content is loading or being retrieved. Maintains layout stability by showing the structure of the component without readable text.

---

## Status

**`Non fonctionnel`** Used for informational or decorative messages not tied to system logic. They are flexible in tone and visual expression, allowing the use of custom or brand-related (decorative) icons depending on context. These alerts help highlight content or support communication in a subtle, branded way.

**⚠️ Note:** Icons in non-functional alerts can be changed or customized depending on the message context.

**`Neutral`** Used for generic informational messages that provide context but carry no semantic meaning. Ideal for subtle notices, contextual help, or content highlights within pages.

**`Accent`** Uses brand colors and can include decorative icons to draw attention to key marketing or communication content. Perfect for promotional, inspirational, or brand-driven highlights that engage the user positively.

**`Fonctionnel`** Used to communicate system statuses, results, or warnings tied directly to UX logic or user actions. These alerts follow strict semantic conventions for icon, color, and tone — ensuring clear, accessible communication across all digital products.

**⚠️ Note:** Icons in functional alerts must never be replaced or customized. Each type has a dedicated, standardized icon that expresses its meaning clearly.

**`Negative`** Indicates a failure, error, or blocking issue that needs user attention. Uses the red "error" color and must include the standardized error icon.

**`Positive`** Confirms that an action was completed successfully. Uses a green color and the standard success icon.

**`Info`** Provides neutral information or updates about the system or account status. Uses blue for neutrality and clarity.

**`Warning`** Draws attention to potential issues or upcoming changes. Uses yellow to signal caution while remaining non-blocking.

---

## Multiline and responsiveness

**Multiline**
This component allows multi-line text editing. The number of lines is not limited.

**Max-width vs full-width**
The max-width is applied to the text within the component.

**User zoom in/out**
The behavior of the text during user zoom in/out must follow a fundamental principle: the text must remain readable, accessible, and must never break the structure or lose information.
* The text must always scale proportionally with user zoom. Text resizing must never be blocked.
* Zooming must never cause text to be truncated or hidden. The component must expand vertically to allow line wrapping.
* The component's height and width must be flexible, never fixed, in order to automatically adapt its dimensions according to the level of zoom.
* Even if, the component has a max-height or a max-width for resizing control purposes, technically, during user zoom in, these limitations are not fixed but must be scalable in order to adapt to the user's zoom level.
* Icons must always scale proportionally with user zoom. Icon resizing must never be blocked.
