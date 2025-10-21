### Property Details (from source)

#### Outlined

**`False`** An input with a subtle background fill and un visible bottom border, creating a softer and more contained look. Best suited for dense layouts or to enhance visibility.

**`True`** A minimalist input with a transparent background and a visible stroke outlining the field. This style may be interesting for contexts other than form pages:
• When inputs need to feel lightweight and unobtrusive
• In a header (search field)
• In a selection/filtering feature in a product catalog

---

#### Rounded corner

**`False`** For a square finish.

**`True`** For a finish with rounded corner. To be favored in more emotional, immersive contexts or those tied to specific visual identities. For standard or business-oriented journeys, keep the default corners. This evolution addresses the need for flexibility in adapting the design to certain brand contexts.

---

#### Error

The default helper text informs the user about the number of digits required. The error state doesn't replace the helper message; instead, it adds a relevant error message beneath the helper text.

Error state applies to all digit inputs simultaneously and cannot be assigned individually.

**False behavior (no error detected)** The user hasn't submitted the form yet, or the form has been submitted and validated successfully. The component displays either in its default state or, if provided, includes a helper text to guide the user.

**True behavior (error detected)** The form was submitted with an invalid PIN code entry. For example, when the user submits without filling all required digits or enters incorrect digits during verification. The component displays two possible error message:
• Empty case: "Please enter the verification code."
• Filled case: "Verification failed. Check and enter the correct code."

⚠️ While the error state is active, the user can type again in the field. Upon resubmission, if validation is successful (True to False), the error state must be removed by resetting it to its default state. When the error state is active, the helper text remains visible without any changes.

---

#### Other boolean options

**Helper text** Offers optional instructional text beneath the PIN code, such as a message indicating the expected number of digits (4, 6, or 8). By default, this text is displayed to inform the user about the required input.

---

**Source Notes**

* Derived from: Figma link (https://www.figma.com/design/QtOWrH1m3RHOAkfyy0XFil/-OUDS-Lib--Components?node-id=67312-34672), uploaded designer document (`pin_code_input_properties.md`)
* Conflicts noted: None.