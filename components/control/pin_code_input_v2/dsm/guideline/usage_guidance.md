## Usage & Guidance

**When should I use outlined vs. filled style for PIN entry?**
Use filled (default) for standard form pages and dense layouts where visibility matters. Switch to outlined for lightweight contexts like header search fields, filtering features, or non-form scenarios where transparency reduces visual weight.  
*See also:* Specs → [Outlined](#outlined), Accessibility → [Visual Accessibility](#visual-accessibility)

**How does auto-advance work when entering digits?**
Focus automatically shifts to the next empty box after typing a valid digit, enabling rapid sequential entry without Tab key presses. Backspace moves focus to the previous box and clears its value, supporting quick corrections during the flow.  
*See also:* Specs → [Length](#length), Accessibility → [Keyboard Support](#keyboard-support)

**When does the error state appear and what triggers it?**
Error activates upon form submission when fields are incomplete or verification fails. Empty case shows "Please enter the verification code."; incorrect entry shows "Verification failed. Check and enter the correct code." Users can retype immediately; successful resubmission clears the error.  
*See also:* Specs → [Error](#error), Accessibility → [Error Handling](#error-handling)

**How should PIN input behave on mobile devices?**
Trigger numeric keyboard using `inputmode="numeric"` to streamline digit entry. Ensure each box meets 44×44px minimum touch target with 8px spacing, and support both portrait and landscape orientations without breaking the layout.  
*See also:* Specs → [Initial settings](#initial-settings), Accessibility → [Touch & Mobile](#touch--mobile)