<<<<<<< HEAD
- **2.1.1 Keyboard** (A): All functionality—entering text, scrolling, accessing helper links, correcting errors—operable via keyboard without timing requirements
- **2.4.7 Focus Visible** (AA): Focus indicator has ≥3:1 contrast on text area border, remains visible during content scrolling and state changes
- **3.3.1 Error Identification** (A): Character limit errors identified in text (not just color) and associated with input via `aria-describedby`
- **3.3.2 Labels or Instructions** (A): Visible labels provided for all text areas, character limits stated in label or helper text, available to assistive technology
- **4.1.2 Name, Role, Value** (A): Semantic `<textarea>` element used, character counter uses `aria-live="polite"`, error states communicated via ARIA attributes
=======
<<<<<<< Updated upstream
- **2.1.1 Keyboard** (A): All text entry, scrolling, and error correction operable via keyboard without timing requirements; Enter key creates new lines rather than submitting forms
- **2.4.7 Focus Visible** (AA): Visible focus indicator with ≥3:1 contrast on text area border when focused, maintained during typing and scrolling
- **3.3.1 Error Identification** (A): Character limit violations and validation errors identified in text, associated via `aria-describedby`, with error icon and red border
- **3.3.2 Labels or Instructions** (A): Labels provided for all text areas, helper text explains character limits upfront, placeholder shows format examples
- **4.1.2 Name, Role, Value** (A): Correct `<textarea>` semantic HTML, `aria-describedby` links helper/error text, `aria-invalid="true"` set during error states
- **4.1.3 Status Messages** (AA): Character counter and limit violations announced via `aria-live="polite"` live region without interrupting typing flow
=======
- **1.3.1 Info and Relationships** (A): Use semantic `<textarea>` element with programmatic label (`<label>` or `aria-labelledby`) and associated descriptions (`aria-describedby`)
- **2.1.1 Keyboard** (A): All functionality including typing, navigation, scrolling operable via keyboard without time limits
- **2.4.7 Focus Visible** (AA): Visible focus indicator with ≥3:1 contrast on interactive textarea element
- **3.3.1 Error Identification** (A): Character limit errors identified in text, associated with input via `aria-describedby`, and explain what's wrong
- **4.1.3 Status Messages** (AA): Character counter updates and error messages announced via ARIA live regions (`aria-live="polite"` for counter, `aria-live="assertive"` for errors)
>>>>>>> Stashed changes
>>>>>>> c9e8b9e (content: update)

For complete reference: [Orange Accessibility Guidelines - Forms Examples](https://a11y-guidelines.orange.com/en/web/components-examples/forms/)