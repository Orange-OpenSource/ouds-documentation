I'll extract the complete English documentation from this Figma frame and transform it to the standard markdown format.

**Process:**
1. Analyzing frame structure...
2. Extracting all sections (excluding WIP and Behaviour and interactions)...
3. Transforming format according to template...
4. Compiling complete documentation...

Let me start by getting a screenshot and metadata to understand the frame structure.Now let me get the metadata to understand the structure of all sections:Perfect! I can see the structure. I can see there's a WIP section at the bottom (node 68601:26063), and I need to check for a "Behaviour and interactions" section. Let me now extract the content from each major section systematically using get_design_context. I'll start with the main sections:

1. Changelog (68467:35571)
2. Definition (68467:35602)
3. Properties (68467:35607)
4. Initial settings (68467:35716)
5. Outlined (68467:35753)
6. Rounded corner (68467:35768)
7. Error (68467:35837)
8. Other boolean options (68467:35888)
9. Behaviour and interactions (68467:35903) - This should be excluded

Let me extract each section:I see the Properties section contains an image/widget. Let me extract the actual properties table content from the widget:Let me try getting the table container:Great! Now let me continue with the other sections:Now let me continue with the remaining sections:Let me continue with the Error and Other boolean options sections:Perfect! Now I have all the content extracted. Let me verify if there's a "Behaviour and interactions" section that I need to exclude. From the screenshot, I can see there's a "Behaviour and interactions" section in red that says "WIP", so I'll exclude that as per the instructions. Let me compile all the content into the standardized markdown format.Perfect! Now let me output the complete documentation in the proper format:

# PIN code input - COMPLETE DOCUMENTATION

---

### Changelog

| Date | Number | Notes | Designer |
|------|--------|-------|----------|
| Sep 30, 2025 | 1.2.0 | • The name of the "Style" variant has been replaced to "Outlined" with true/false variant | Hamza Amarir |
| Jul 29, 2025 | 1.1.0 | • Several design token updates: [Component tokens changelog 1.5.0](https://www.figma.com/design/Co2t6wHMf4GB9NJVGs2Hes/-OUDS-Core-Lib--Design-tokens?m=auto&node-id=9280-2568&t=HLVB4jOd35DWr8Bj-1) | Maxime Tonnerre |
| Jun 30, 2025 | 1.0.0 | • Component creation | Maxime Tonnerre |

---

### Definition

A PIN code input is a specialized form field used to capture short, fixed-length numeric codes, typically for authentication or confirmation purposes, such as a 4, 6 or 8-digit personal identification number (PIN).

It is often presented as a series of individual input fields or boxes, each representing a single digit, to enhance readability and encourage accurate input.

This component must support smooth keyboard navigation (automatic focus shift, backspace handling), secure input masking if needed. It is commonly used in sensitive flows like login, verification, or transaction confirmation.

---

### Properties

| property name | type |
|---------------|------|
| Outlined | 'False' \| 'True' |
| Rounded corner | 'False' \| 'True' |
| Length | '4' \| '6' \| '8' |
| Error | 'False' \| 'True' |
| Helper text | boolean |
| ✏️ Helper text (4 digit code) | text |
| ✏️ Helper text (6 digit code) | text |
| ✏️ Helper text (8 digit code) | text |

---

### Initial settings

**Outlined** Off

**Rounded corner** Off

**Length** 6

**Error** Off

**Helper text** Off

---

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

The Error status indicates that the user input does not meet validation rules or expected formatting. It provides immediate visual feedback, typically through a red border, error icon, and a clear, accessible error message positioned below the input (mandatory).

This state helps users quickly identify and correct mistakes by explaining what went wrong and, when possible, how to fix it. The input remains editable, encouraging users to revise their input without starting over.

The error state must be triggered by an explicit validation (submission, API response), and not in real time with each keystroke. This can occur either because the entered code does not match the expected code, because the user entered an expired or already used code, or finally if the maximum number of attempts has been exceeded.

⚠️ **Alert:** In the context of a PIN code input, in addition to the input's "Error" UI rendering, it is essential to also include an "Alert" component (also in its "Error" status) in the interface.

---

### Other boolean options

**Helper text** Supporting text conveys additional information about the input field, such as how it will be used. It should ideally only take up a single line, though may wrap to multiple lines if required, and be either persistently visible or visible only on focus.