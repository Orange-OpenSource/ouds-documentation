**`Suffix`** An element placed after the user's input, often used to display a currency or a unit (kg, %, cm…).

**`Helper text`** Supporting text conveys additional information about the input field, such as how it will be used. It should ideally only take up a single line, though may wrap to multiple lines if required, and be either persistently visible or visible only on focus.

### Do & don'ts

✅ **Do:** Use suffix for units of measurement (kg, cm, %) or currency symbols that clarify the value's meaning  
❌ **Don't:** Place units in the label or helper text when a suffix provides clearer inline context

✅ **Do:** Keep helper text brief and focused on a single piece of guidance (e.g., "Maximum 99 items")  
❌ **Don't:** Overload helper text with multiple instructions—prioritize the most critical information

✅ **Do:** Associate helper text with the input using `aria-describedby` for screen reader accessibility  
❌ **Don't:** Position helper text far from the input where the visual association becomes unclear

✅ **Do:** Show helper text persistently when the information is essential for correct input  
❌ **Don't:** Hide critical guidance behind focus states where users may miss it

✅ **Do:** Ensure suffix text maintains legibility and doesn't crowd the numeric value  
❌ **Don't:** Use long suffix text that causes truncation or makes the input feel cramped