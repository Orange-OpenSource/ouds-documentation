**Keyboard input disabled**

In the vast majority of modern UX/UI cases, a quantity input should be editable on focus. However, there are a few specific rare cases where direct editing by keyboard input might be disabled:
• Highly guided or controlled usage→product configuration with mandatory steps
• Risk of critical error→specific or technical values
• Strict touch context→mobile app with simplified UI, no keyboard
• Deliberate product decision→to enforce navigation or a business constraint

In this specific context, it is therefore recommended to prefill the input by default.

**Keyboard input + increment/decrement controls enabled**

In the context of an editable quantity input, if the field is focused and already filled by the user, then clicking the + (increase) or – (decrease) buttons must follow a smooth and predictable behavior according to the following UX rules.

When clicking + or – during editing:
• The value is automatically validated
• The action is applied to that value (+1 or –1)
• The field is visually updated with the new value
• The cursor is moved to the end of the field (optional)
• The field remains focused

Absolutely to avoid:
• Losing the currently typed value if partially entered
• Requiring defocus for the buttons to work
• Failing to parse/validate the value before incrementing

Specific error focus state:
If the value in the field is invalid (empty or non-numeric), clicking + or – may:
• Either fill in a default value (1)
• Or display a temporary blocking error ("Please enter a number")

### Do & don'ts

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