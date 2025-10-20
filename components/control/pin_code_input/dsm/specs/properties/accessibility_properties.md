### Accessibility Properties

**Label Association**  
Must include proper label text (visible or screen-reader only) explaining the purpose of the code input, such as "Enter 6-digit verification code."

**Error Messages**  
Error states must be accompanied by descriptive error messages that are programmatically associated with the input and announced to screen readers.

**Live Region Announcements**  
Status updates (such as "Code accepted" or "Invalid code") should be announced to screen readers through ARIA live regions.

**Cell Labels**  
Each input cell should have appropriate ARIA labels indicating its position, such as "Digit 1 of 6."