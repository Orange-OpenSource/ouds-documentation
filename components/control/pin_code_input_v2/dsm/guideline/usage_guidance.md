## Usage & Guidance

**How should I configure labels and helper text for SMS verification codes?**  
Position a descriptive label above the input fields (e.g., "Enter verification code") and include helper text below showing the destination phone number or explaining the code source.

**What should the error state look like when a code is invalid?**  
Display red borders around all input fields, show an error icon, and provide a specific error message below explaining whether the code was incorrect, expired, or the maximum attempts were exceeded.

**How do I display different PIN lengths for various use cases?**  
Use 4 fields for simple PINs or quick verification, 6 fields for standard authentication codes (SMS/email), and 8 fields for enhanced security scenarios requiring longer codes.

**How should the component appear during active digit entry?**  
Highlight the current input field with a focus indicator, auto-advance to the next field after each digit is entered, and allow backspace to move to the previous field for corrections.