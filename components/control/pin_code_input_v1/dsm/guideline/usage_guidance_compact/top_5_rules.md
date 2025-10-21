### Top 5 Rules

**Auto-advance focus (Must)**

* ✅ **Do:** Move focus to the next digit automatically upon valid character entry
  *Reduces friction and matches user mental model of sequential entry.*
* ❌ **Don't:** Require manual Tab navigation between digit boxes
  *Forces unnecessary keystrokes and slows completion.*

**Backspace behavior (Must)**

* ✅ **Do:** Clear current digit and move focus to previous box on Backspace
  *Allows natural correction flow without losing position.*
* ❌ **Don't:** Delete current digit but leave focus in place
  *Breaks expected editing pattern and confuses users.*

**Paste support (Should)**

* ✅ **Do:** Accept full code via paste and distribute across digit boxes (e.g., from SMS)
  *Enables fast autofill and reduces manual entry errors.*
* ❌ **Don't:** Block paste or insert all digits into the first box only
  *Forces tedious retyping when autofill is available.*

**Unified error state (Must)**

* ✅ **Do:** Apply error styling to all digit boxes simultaneously with `aria-invalid="true"`
  *Communicates validation failure as a single cohesive event.*
* ❌ **Don't:** Highlight only the first empty or incorrect digit
  *Implies individual validation when the code is validated as a whole.*

**Helper text visibility (Should)**

* ✅ **Do:** Display digit count ("Enter 6-digit code") by default; append error below without replacing it
  *Preserves guidance while adding failure context.*
* ❌ **Don't:** Replace helper text entirely with error message
  *Removes the digit count reference users need for correction.*

*See also:* Specs → Initial Config, Accessibility → Error Handling, Accessibility → Keyboard Support