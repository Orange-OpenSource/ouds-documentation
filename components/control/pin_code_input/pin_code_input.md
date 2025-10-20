# Guideline

## Intro
A specialized input field for entering numeric verification codes, typically used in multi-factor authentication and security workflows.

---

## What is it
The Pin Code Input component is a specialized numeric input field designed specifically for entering verification codes, PINs, and one-time passwords (OTPs). Unlike standard text inputs, it provides a segmented visual structure where each digit occupies its own distinct cell, creating a clear, focused interface for code entry. This component automatically manages digit progression, visual feedback for each character position, and supports various input methods including keyboard entry, paste operations, and auto-fill from SMS or authenticator apps. The structured layout makes it immediately clear how many digits are expected and which positions have been filled, significantly reducing entry errors and improving the user experience during security verification processes. It includes built-in error states for invalid codes and supports both filled and outlined visual styles to match different design systems.

---

## Anatomy

| # | Element | Purpose |
|---|---------|---------|
| 1 | Container | Groups all input cells into a unified component structure |
| 2 | Input Cells | Individual digit containers that display entered characters |
| 3 | Cell Borders | Visual boundaries that define each digit position |
| 4 | Focus Indicator | Highlights the currently active input cell |
| 5 | Character Display | Shows the entered digit or placeholder state |
| 6 | Error State Indicator | Visual feedback for invalid code entries |

---

## Key Features

**Segmented Input Structure**  
Each digit occupies a dedicated cell, providing clear visual separation and making it obvious how many characters are required.

**Auto-progression**  
Automatically advances focus to the next cell when a digit is entered, streamlining the input process without requiring manual navigation.

**Paste Support**  
Accepts complete codes pasted from clipboard or auto-filled from SMS/email, intelligently distributing digits across cells.

**Error State Management**  
Displays clear visual feedback when an invalid code is entered, helping users identify and correct mistakes quickly.

**Flexible Length Configuration**  
Supports various code lengths (typically 4-8 digits) to accommodate different security requirements and verification systems.

---

## When to Use

Use the Pin Code Input component when you need to:

✅ Verify user identity through SMS, email, or authenticator app codes during login or sensitive operations.

✅ Collect numeric PINs for account security, payment authorization, or access control systems.

✅ Enable two-factor authentication workflows where users need to enter time-based or event-based verification codes.

✅ Implement password reset flows that require email or SMS verification before allowing password changes.

✅ Authenticate transactions in banking or financial applications where numeric codes provide additional security.

---

## When not to Use

Avoid using this component when:

❌ Users need to enter alphanumeric codes that include letters, as this component is optimized for numeric-only input.

❌ The input is for general text entry like names, addresses, or messages where a standard text field is more appropriate.

❌ You need to collect sensitive information that shouldn't be displayed character-by-character, such as full passwords or credit card numbers.

❌ The verification process involves pattern recognition or gesture-based authentication rather than code entry.

❌ Users need to enter variable-length codes where the expected number of digits is unknown or flexible.

---

## Common Patterns

**Two-Factor Authentication**  
Used during login flows after username/password entry to verify identity through a time-based code from an authenticator app or SMS.

**Account Recovery**  
Appears in password reset workflows where users receive a verification code via email or SMS to confirm account ownership before setting a new password.

**Transaction Verification**  
Integrated into payment or transfer confirmation screens in banking apps where users enter a code to authorize sensitive financial operations.

---

## Screen Variants

**Desktop**  
Input cells are sized for comfortable mouse/keyboard interaction with clear spacing between cells and prominent focus indicators for keyboard navigation.

**Tablet**  
Cell sizes increase slightly to accommodate touch input while maintaining visual clarity, with optimized spacing for stylus or finger interaction.

**Mobile**  
Cells are enlarged to meet minimum touch target requirements (44x44px) with appropriate spacing, and numeric keyboard automatically appears on focus.

---

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

---

# Accessibility

### Keyboard Navigation

The component must support full keyboard accessibility with intuitive navigation between cells. Users should be able to tab into the component, which focuses the first empty cell (or first cell if all are empty). Arrow keys (Left/Right) should move focus between cells, allowing users to navigate freely to correct mistakes. Backspace should delete the current cell's content and move focus to the previous cell, while Delete should clear the current cell without moving focus. The Tab key should move focus out of the component to the next focusable element on the page. All focus indicators must meet a minimum contrast ratio of 3:1 against adjacent colors and be clearly visible, typically using a 2-3px outline or border highlight. When errors occur, focus should remain on or return to the first cell to allow easy re-entry.

---

### Screen Reader Support

Each input cell must be implemented as a proper form input element (input type="text" with inputmode="numeric") with semantic HTML ensuring native screen reader support. The component container should have a role="group" with an accessible name describing its purpose (e.g., "Verification code input"). Each individual cell must have an accessible label indicating its position, such as "Digit 1 of 6" using aria-label or aria-labelledby. When a digit is entered, screen readers should announce the entered value and automatically indicate focus has moved to the next cell. Error states must use aria-invalid="true" on affected cells with associated error messages linked via aria-describedby. Status messages (like "Code accepted" or "Invalid code") should be announced through ARIA live regions (aria-live="polite" for non-urgent messages, aria-live="assertive" for critical errors).

---

### ARIA Attributes

The component requires several ARIA attributes for proper accessibility. The container must use role="group" with aria-labelledby pointing to the component's label element. Each input cell should include aria-label="Digit [X] of [Y]" to indicate position within the sequence. When in error state, cells must have aria-invalid="true" and aria-describedby pointing to the error message element's ID. If using helper text, associate it with the component using aria-describedby on the container. For auto-complete functionality, cells should include autocomplete="one-time-code" to enable browser/OS-level code detection from SMS. Status updates should use aria-live="polite" for general messages and aria-live="assertive" for critical errors, ensuring announcements don't interrupt current screen reader activity unnecessarily.

---

### Focus Management

Focus must be managed programmatically throughout the interaction lifecycle. On component mount, if auto-focus is enabled, focus should move to the first input cell automatically. When a digit is entered, focus should automatically advance to the next empty cell. When Backspace is pressed, focus should move to the previous cell after clearing the current one. If users navigate with arrow keys, focus should move appropriately between cells. When validation occurs and an error is detected, focus should return to the first cell to allow easy re-entry of the complete code. Focus indicators must be clearly visible with sufficient contrast (minimum 3:1 ratio) and typically implemented as a 2-3px colored border or outline. Focus should never be trapped within the component—users must always be able to tab out to other page elements. When the component is disabled, it should not receive focus at all.

---

### Error Handling

Error states must be communicated through multiple channels for accessibility. Visual changes alone (color shifts) are insufficient—errors must be programmatically announced to screen readers using aria-live regions. Each input cell in error state should have aria-invalid="true" applied. A descriptive error message must appear below the component and be associated via aria-describedby on the input cells, with messages like "The code you entered is invalid. Please check your messages and try again." The error message element should have role="alert" or be within an element with aria-live="assertive" to ensure immediate announcement. Focus should return to the first input cell when an error occurs, allowing users to easily re-enter the code. Error messages should be persistent (not automatically dismissed) until the user begins correcting the input. Color contrast for error text must meet WCAG requirements (4.5:1 for normal text).

---

### Touch Targets

All interactive elements must meet minimum touch target size requirements for mobile accessibility. Each input cell should be at least 44x44 pixels (iOS standard) or 48x48 pixels (Android standard) to ensure comfortable touch interaction. Spacing between adjacent cells should be sufficient (minimum 8px) to prevent accidental taps on neighboring cells. On mobile devices, tapping any cell should bring up the numeric keyboard automatically with inputmode="numeric" or type="tel" on the input elements. The entire component should be positioned with adequate spacing from other interactive elements on the page (minimum 8px clearance) to prevent mis-taps. For tablet devices, consider slightly larger target sizes (48-52px) to accommodate stylus input. Touch targets should include visual feedback on tap (such as brief background color change) to confirm interaction.

---

### Color Contrast

All text and interactive elements must meet WCAG 2.1 AA contrast requirements. Input cell borders must have a contrast ratio of at least 3:1 against adjacent backgrounds for both filled and outlined variants. Text content within cells (entered digits) must meet 4.5:1 contrast for normal text or 3:1 for large text (18px+ regular or 14px+ bold). Placeholder indicators or empty cell backgrounds must provide sufficient contrast to be perceivable. Focus indicators must have a minimum 3:1 contrast ratio against both the cell background and the surrounding page background. Error states must not rely solely on color—red borders for errors must be accompanied by text messages and/or iconography. When using color to indicate states (focused, filled, error), ensure each state is distinguishable by at least one additional non-color characteristic (border width, icon, pattern). Test the component in both light and dark modes to ensure contrast requirements are met in all themes.

---

### Component-Specific Considerations

The Pin Code Input has unique accessibility requirements beyond standard form inputs. Since it presents a single logical input split across multiple visual cells, screen readers must understand it as a unified code entry field rather than separate, unrelated inputs. Use role="group" on the container with a clear accessible name to establish this relationship. The component must handle auto-fill from SMS and authenticator apps accessibly—when a code is auto-populated, screen readers should announce "Code automatically entered" or similar confirmation. For security reasons, consider whether to implement masking (showing dots instead of numbers after entry)—if implemented, provide a "Show/Hide code" toggle that's keyboard accessible and properly announced. Time-limited codes should include accessible timer announcements ("Code expires in 30 seconds") without interrupting the input process. If the component includes a "Resend code" button, ensure it's keyboard accessible, has clear focus indication, and announces its state (disabled/enabled) and any cooldown periods ("Resend available in 30 seconds").