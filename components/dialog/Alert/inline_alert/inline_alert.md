# Guideline

## Intro 👈🤖

Inline Alert is a lightweight, embedded notification component that delivers contextual feedback within the content flow without interrupting user workflow.

---

## Definition

Inline Alert is a lightweight, embedded alert used within the content flow (e.g. inside a form, card, settings section). It is less visually prominent than Alert Message and does not include a dismiss button.

---

## Best for 👈🤔

✅ Providing contextual feedback within forms, cards, or settings sections without disrupting user flow

✅ Displaying validation messages that aggregate feedback related to multiple fields

✅ Communicating system status updates (success, error, warning, info) in a non-intrusive manner

✅ Highlighting important information or instructions close to relevant content areas

✅ Showing persistent messages that remain visible until the underlying condition changes

✅ Delivering promotional or brand-driven highlights in a subtle, embedded format

✅ Informing users about temporary conditions or feature availability within a specific section

✅ Providing neutral informational context or help text within page layouts

✅ Alerting users to potential issues before they take an action (warning scenarios)

✅ Confirming successful completion of actions without modal interruption

---

## Anatomy 👈🤖

| # | Element | Purpose | Optional |
|---|---------|---------|----------|
| 1 | Container | Wraps all alert content and provides visual boundary with semantic color | N |
| 2 | Status icon | Reinforces message severity through standardized iconography | Y |
| 3 | Text message | Communicates the alert content in a concise, scannable format | N |
| 4 | Background fill | Provides visual emphasis and semantic color coding for status type | N |
| 5 | Left border accent | Emphasizes severity through colored vertical stripe (combined) | Y |

---

## State

**`Enabled`** Displayed when the inline alert is active and content is available. Shows an icon and short text message to provide immediate, contextual feedback within the interface.

**`Skeleton`** Used as a placeholder while the alert content is loading or being retrieved. Maintains layout stability by showing the structure of the component without readable text.

---

## state_do_&_dont 👈🤔

✅ **Do:** Use the skeleton state during asynchronous content loading to maintain layout stability and prevent content shifting  
❌ **Don't:** Show an empty container or leave blank space while alert content is being fetched

✅ **Do:** Ensure the enabled state is immediately visible when content becomes available without unnecessary animation delays  
❌ **Don't:** Add excessive entrance animations that slow down the display of important alert information

✅ **Do:** Maintain consistent dimensions between skeleton and enabled states to prevent layout jumps  
❌ **Don't:** Allow the skeleton placeholder to have different proportions than the final rendered alert

✅ **Do:** Use skeleton states only for genuinely asynchronous content that requires loading time  
❌ **Don't:** Display skeleton placeholders for static alerts that can be rendered immediately

✅ **Do:** Provide clear visual distinction between skeleton and enabled states so users understand content is loading  
❌ **Don't:** Make skeleton states so subtle that users cannot distinguish them from broken or missing content

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

## status_do_&_dont 👈🤔

✅ **Do:** Match the alert status variant (negative, positive, info, warning) to the semantic meaning of the message content  
❌ **Don't:** Use a positive (success) variant to display error messages or vice versa, as this confuses users

✅ **Do:** Use standardized, non-customizable icons for functional alerts (negative, positive, info, warning) to ensure consistent recognition  
❌ **Don't:** Replace or customize icons in functional alerts, as this breaks semantic conventions and reduces accessibility

✅ **Do:** Reserve accent variants for promotional or brand-driven highlights that engage users positively without system urgency  
❌ **Don't:** Use accent or decorative variants for critical system messages that require immediate user attention

✅ **Do:** Use the neutral variant for generic informational messages that don't carry semantic weight or urgency  
❌ **Don't:** Overuse colored status variants for messages that are purely informational, as this dilutes their impact

✅ **Do:** Ensure negative (error) alerts clearly indicate what went wrong and provide actionable next steps when possible  
❌ **Don't:** Display vague error messages without context or guidance on how to resolve the issue

---

# Specs

## States

**`Enabled`** Displayed when the inline alert is active and content is available. Shows an icon and short text message to provide immediate, contextual feedback within the interface.

**`Skeleton`** Used as a placeholder while the alert content is loading or being retrieved. Maintains layout stability by showing the structure of the component without readable text.

---

## Layout and spacing

🚧 Content to be added

---

# Changelog

| Date | Number | Notes | Designer |
|------|--------|-------|----------|
| Oct 14, 2025 | 1.0.0 | • Component creation | Anton Astafev |
