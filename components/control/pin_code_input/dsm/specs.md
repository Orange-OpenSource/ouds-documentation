# Specs

## Properties

### Initial Config

| Property | Default Value | Notes |
|----------|---------------|-------|
| Variant | Filled | Can be set to Outlined for different visual styles |
| Length | 6 | Number of digit cells (typically 4-8) |
| State | Default | Can be Error for invalid codes |
| Auto-focus | True | Automatically focuses first cell on mount |
| Numeric Only | True | Restricts input to digits 0-9 |

### Variant

**Filled**  
The default visual style featuring cells with background fills that provide clear definition between input positions. This variant works well on both light and dark backgrounds and offers strong visual hierarchy.

**Outlined**  
An alternative style using border-only cells without background fills, creating a lighter, more minimal appearance. This variant is ideal for designs requiring visual subtlety or when placed on colored backgrounds.

---

### State

**Default**  
The standard appearance when the component is ready for input, with neutral colors indicating an inactive or partially-filled state.

**Focused**  
Applied to the currently active cell, displaying enhanced visual indicators (typically through border color, background change, or shadow) to show where the next digit will be entered.

**Filled**  
Indicates cells that contain entered digits, typically showing a different visual treatment to distinguish completed positions from empty ones.

**Error**  
Activated when an invalid code is submitted or validation fails, applying error colors (typically red) to all cells to clearly communicate the issue.

**Disabled**  
Renders the component in a non-interactive state with reduced opacity, used when code entry is temporarily unavailable or pending another action.

---

### Length

Defines the number of digit cells displayed in the component, typically ranging from 4 to 8 digits depending on security requirements:

- **4 digits**: Common for basic PINs and simple verification codes
- **6 digits**: Standard for most OTP and 2FA implementations (TOTP standard)
- **8 digits**: Used for high-security applications or certain authenticator systems

The length should be set based on the security requirements of your authentication system and cannot be changed during runtime.

---

### Behavioral Properties

**Auto-focus on Mount**  
When enabled, automatically focuses the first input cell when the component appears, allowing users to immediately start typing without clicking.

**Auto-progression**  
Automatically moves focus to the next empty cell when a digit is entered, enabling rapid input without manual navigation.

**Auto-submit on Complete**  
Optionally triggers validation or form submission automatically when all cells are filled, streamlining the verification process.

**Paste Handling**  
Intelligently processes pasted content by extracting numeric characters and distributing them across cells, supporting auto-fill from SMS and password managers.

**Clear on Error**  
Optionally clears all cells when an error occurs, allowing users to re-enter the code cleanly rather than correcting individual digits.

---

### Accessibility Properties

**Label Association**  
Must include proper label text (visible or screen-reader only) explaining the purpose of the code input, such as "Enter 6-digit verification code."

**Error Messages**  
Error states must be accompanied by descriptive error messages that are programmatically associated with the input and announced to screen readers.

**Live Region Announcements**  
Status updates (such as "Code accepted" or "Invalid code") should be announced to screen readers through ARIA live regions.

**Cell Labels**  
Each input cell should have appropriate ARIA labels indicating its position, such as "Digit 1 of 6."

---

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