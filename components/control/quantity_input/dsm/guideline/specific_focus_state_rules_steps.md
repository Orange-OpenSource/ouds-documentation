**Keyboard input + increment/decrement controls enabled**

In the context of an editable quantity input, if the field is focused and already filled by the user, then clicking the + (increase) or – (decrease) buttons must follow a smooth and predictable behavior according to the following UX rules.

**When clicking + or – during editing:**
* The value is automatically validated
* The action is applied to that value (+1 or –1)
* The field is visually updated with the new value
* The cursor is moved to the end of the field (optional)
* The field remains focused

**Absolutely to avoid:**
* Losing the currently typed value if partially entered
* Requiring defocus for the buttons to work
* Failing to parse/validate the value before incrementing

**Specific error focus state:**  
If the value in the field is invalid (empty or non-numeric), clicking + or – may:
* Either fill in a default value (1)
* Or display a temporary blocking error ("Please enter a number")
