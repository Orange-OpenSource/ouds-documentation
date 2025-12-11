## Definition

Inline Alert is a lightweight, embedded alert used within the content flow (e.g. inside a form, card, settings section). It is less visually prominent than Alert Message and does not include a dismiss button.

---

## State

**`Enabled`** Displayed when the inline alert is active and content is available. Shows an icon and short text message to provide immediate, contextual feedback within the interface.

**`Skeleton`** Used as a placeholder while the alert content is loading or being retrieved. Maintains layout stability by showing the structure of the component without readable text.

---

## Status

**Non fonctionnel** Used for informational or decorative messages not tied to system logic. They are flexible in tone and visual expression, allowing the use of custom or brand-related (decorative) iconsdepending on context. These alerts help highlight content or support communication in a subtle, branded way.

**⚠️ Note:** Icons in non-functional alerts can be changed or customized depending on the message context.

**`Neutral`** Used for generic informational messages that provide context but carry no semantic meaning. Ideal for subtle notices, contextual help, or content highlights within pages.

**`Accent`** Uses Orange brand colors and can include decorative icons to draw attention to key marketing or communication content. Perfect for promotional, inspirational, or brand-driven highlights that engage the user positively.

**Fonctionnel** Used to communicate system statuses, results, or warnings tied directly to UX logic or user actions. These alerts follow strict semantic conventions for icon, color, and tone — ensuring clear, accessible communication across all Orange digital products.

**⚠️ Note:** Icons in functional alerts must never be replaced or customized. Each type has a dedicated, standardized icon that expresses its meaning clearly.

**`Negative`** Indicates a failure, error, or blocking issue that needs user attention. Uses the red "error" color and must include the standardized error icon.

**`Positive`** Confirms that an action was completed successfully. Uses a green color and the standard success icon.

**`Info`** Provides neutral information or updates about the system or account status. Uses blue for neutrality and clarity.

**`Warning`** Draws attention to potential issues or upcoming changes. Uses yellow to signal caution while remaining non-blocking.

---
