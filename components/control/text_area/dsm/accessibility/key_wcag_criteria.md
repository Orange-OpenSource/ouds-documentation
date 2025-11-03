- **2.1.1 Keyboard** (A): All text entry, scrolling, and error correction operable via keyboard without timing requirements; Enter key creates new lines rather than submitting forms
- **2.4.7 Focus Visible** (AA): Visible focus indicator with ≥3:1 contrast on text area border when focused, maintained during typing and scrolling
- **3.3.1 Error Identification** (A): Character limit violations and validation errors identified in text, associated via `aria-describedby`, with error icon and red border
- **3.3.2 Labels or Instructions** (A): Labels provided for all text areas, helper text explains character limits upfront, placeholder shows format examples
- **4.1.2 Name, Role, Value** (A): Correct `<textarea>` semantic HTML, `aria-describedby` links helper/error text, `aria-invalid="true"` set during error states
- **4.1.3 Status Messages** (AA): Character counter and limit violations announced via `aria-live="polite"` live region without interrupting typing flow

For complete reference: [Orange Accessibility Guidelines - Form Components](https://a11y-guidelines.orange.com/en/web/components-examples/forms/)