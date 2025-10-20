## Usage

### Cell Spacing
**Do:** Maintain consistent spacing between cells (typically 8-12px) to clearly distinguish individual digit positions while keeping the component visually cohesive.

**Don't:** Place cells too close together where they appear as a single input field, or space them so far apart that they don't feel like a unified component.

---

### Error Communication
**Do:** Combine visual error states (red cells) with clear error messages below the component explaining what went wrong, such as "Invalid code. Please try again."

**Don't:** Rely solely on color changes to indicate errors without providing text explanations, as this excludes colorblind users.

---

### Code Length Clarity
**Do:** Make the expected code length obvious through the number of visible cells and include helper text if needed, such as "Enter the 6-digit code sent to your phone."

**Don't:** Create ambiguity about how many digits are required or allow variable-length input without clear guidance.

---

### Input Method Support
**Do:** Support multiple input methods including typing, pasting, and auto-fill from SMS/authenticator apps to accommodate different user workflows.

**Don't:** Restrict users to only manual digit-by-digit entry when paste and auto-fill capabilities would significantly improve the experience.