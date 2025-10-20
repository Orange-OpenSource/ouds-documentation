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