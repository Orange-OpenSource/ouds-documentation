✅ **Do:** Maintain focus on the input field when users interact with increment/decrement buttons  
❌ **Don't:** Move focus away from the quantity input after button clicks, disrupting keyboard navigation flow

✅ **Do:** Validate and apply the current value before incrementing or decrementing when the field is being edited  
❌ **Don't:** Ignore partially entered values—parse and validate them before applying the step change

✅ **Do:** Provide a clear focus indicator that encompasses the entire control (input + buttons) as a single unit  
❌ **Don't:** Show separate focus states for the input and buttons, confusing users about the component boundary

✅ **Do:** Support keyboard shortcuts (Arrow Up/Down) for incrementing and decrementing when the input has focus  
❌ **Don't:** Require users to tab to buttons separately when keyboard arrow controls can serve the same purpose

✅ **Do:** Handle edge cases gracefully—default to minimum value (1) when the field is empty and user clicks increment  
❌ **Don't:** Throw errors or behave unpredictably when users click buttons on an empty or invalid input