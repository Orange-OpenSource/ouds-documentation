# PIN code input - Behavior

---

### Behaviour and interactions

**Visible or Accessible Label**
• The input must have a clear and unique label, either visible on screen or provided through aria-label or aria-labelledby.
• Never rely solely on a placeholder to describe the field — placeholders do not replace labels, especially for screen reader users.

**Clear separation of country selector, dial code, and input field**
• The country selector must be keyboard-navigable (e.g., <button> or <select>) and properly labelled (e.g., aria-label="Select country").
• If the dial code (e.g., +33) is displayed as a prefix, it should be readable by assistive technologies, with a clear semantic role (e.g., non-editable text, not focusable if decorative).
• Ensure the visual and semantic reading order is coherent (e.g., "Select country, France, plus thirty-three, phone number").

**Input formatting and guidance**
• If a mask is used for formatting (e.g., (0X) XX XX XX XX), it must not interfere with keyboard navigation or screen reader output.
• Provide clear instructions if a specific format is required, both visually and via aria-describedby.

**Clear and accessible error feedback**
• In case of errors (e.g., incomplete number, invalid format), display a clear, visible error message, linked to the field via aria-describedby.
• Do not rely on color alone to indicate errors — combine text, icon, and visual state changes.

**Smooth keyboard navigation**
• All interactive elements (input field, country selector, etc.) must be fully keyboard-accessible in a logical order (e.g., using Tab and arrow keys).
• Follow native interaction patterns (e.g., use arrow keys to navigate country list, Escape to close dropdown, etc.).

**Logical screen reader announcements**
• Ensure screen readers announce elements in a clear and logical order: field label, selected country, dial code, and then the input field.
• Avoid complex composite fields that may not be well supported by assistive technologies. Prefer either a single field or clearly separated elements with appropriate ARIA roles.

**Responsive and readable at all scales**
• The component must remain readable and functional at all screen sizes, including zoom (up to 200%, per WCAG 2.2 AA) or in compact interfaces.
• Related elements (label, icons, helper text, error messages) must remain visible, legible, and non-overlapping.
• All field elements must remain functional under zoom: input, focus, keyboard interactions, visibility of states (error, helper, etc.).
• No element (e.g., error message, action icon) should be truncated, hidden, or inaccessible due to zoom.
• On mobile, pinch-to-zoom must be allowed (avoid meta tags like user-scalable=no).
• Prefer column-based or flex-wrap layouts to prevent horizontal breaking.
• Icons and interactive elements must scale with text during zoom.
• Ensure touch targets remain large enough: at least 44x44 px in final display, regardless of scale.

---

⚠️ **Note:** This section is marked as WIP (Work in Progress) in the Figma file.

---
