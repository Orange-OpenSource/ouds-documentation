## Properties

### Initial Config

| Property | Default Value | Notes |
|----------|---------------|-------|
| Outlined | False | Filled style provides better visibility in dense layouts; outlined reduces visual weight for non-form contexts. |
| Rounded corner | False | Square corners suit standard/business flows; rounded corners offer flexibility for brand-specific or emotional contexts. |
| Length | 6 | Six digits balances security and usability; adjust to 4 or 8 based on system requirements. |
| Error | False | Error state applies to all boxes simultaneously and cannot be assigned individually. |
| Helper text | Off | When enabled, displays the expected digit count (4, 6, or 8) to guide user input. |

---

### Property Details (from source)

### Outlined

**`False`** An input with a subtle background fill and un visible bottom border, creating a softer and more contained look. Best suited for dense layouts or to enhance visibility.

**`True`** A minimalist input with a transparent background and a visible stroke outlining the field. This style may be interesting for contexts other than form pages:
• When inputs need to feel lightweight and unobtrusive
• In a header (search field)
• In a selection/filtering feature in a product catalog

---

### Rounded corner

**`False`** For a square finish.

**`True`** For a finish with rounded corner. To be favored in more emotional, immersive contexts or those tied to specific visual identities. For standard or business-oriented journeys, keep the default corners. This evolution addresses the need for flexibility in adapting the design to certain brand contexts.

---

### Error

The default helper text informs the user about the number of digits required. The error state doesn't replace the helper message; instead, it adds a relevant error message beneath the helper text.

Error state applies to all digit inputs simultaneously and cannot be assigned individually.

**False behavior (no error detected)** The user hasn't submitted the form yet, or the form has been submitted and validated successfully. The component displays either in its default state or, if provided, includes a helper text to guide the user.

**True behavior (error detected)** The form was submitted with an invalid PIN code entry. For example, when the user submits without filling all required digits or enters incorrect digits during verification. The component displays two possible error message:
• Empty case: "Please enter the verification code."
• Filled case: "Verification failed. Check and enter the correct code."

⚠️ While the error state is active, the user can type again in the field. Upon resubmission, if validation is successful (True to False), the error state must be removed by resetting it to its default state. When the error state is active, the helper text remains visible without any changes.

---

### Other boolean options

**Helper text** Offers optional instructional text beneath the PIN code, such as a message indicating the expected number of digits (4, 6, or 8). By default, this text is displayed to inform the user about the required input.

---

### Length

| Property Value | Notes |
|----------------|-------|
| 4 | Four-digit PIN for quick authentication scenarios (e.g., app unlock, simple verification). |
| 6 | Six-digit PIN balances security and usability (default); common for two-factor authentication flows. |
| 8 | Eight-digit PIN for high-security contexts (e.g., transaction confirmation, sensitive account access). |

---

**Source Notes**

* Derived from: [Figma Component](https://www.figma.com/design/QtOWrH1m3RHOAkfyy0XFil/-OUDS-Lib--Components?node-id=67312-34672), uploaded designer document (pin_code_input_properties.md)
* Conflicts noted: None.