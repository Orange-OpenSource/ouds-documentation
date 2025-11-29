**Prefix** A visual or textual element placed before the user's input. A prefix is not common and is discouraged in a Password Input component. Here are illustrative examples of very specific cases where:
• "corp-" Company password enforcing a prefix
• "temp-" Temporary password during a testing phase
• "dev-" For test accounts
• "eu-, us-, prod-, stage-" To encode a target environment
• "test@" Used in the context of automated or predictable tests
• "admin-" Pattern used to define an admin password

**Helper text** Supporting text conveys additional information about the input field, such as how it will be used. It should ideally only take up a single line, though may wrap to multiple lines if required, and be either persistently visible or visible only on focus.

### Do & don'ts

✅ **Do:** Use helper text to communicate password requirements upfront (e.g., minimum length, required character types).  
❌ **Don't:** Hide critical password requirements in tooltips or only reveal them after validation failures.

✅ **Do:** Keep helper text concise—ideally one line—while still providing actionable guidance.  
❌ **Don't:** Overload helper text with every possible requirement, making it overwhelming to read.

✅ **Do:** Connect helper text programmatically to the input via `aria-describedby` for screen reader accessibility.  
❌ **Don't:** Position helper text far from the input where the visual association becomes unclear.

✅ **Do:** Reserve prefixes for very specific enterprise or system contexts where they're genuinely required by backend systems.  
❌ **Don't:** Use prefixes in consumer-facing password fields as they add unnecessary complexity and confusion.

✅ **Do:** Display password strength indicators or requirement checklists as helper content to guide secure password creation.  
❌ **Don't:** Show helper text and error messages simultaneously—error messages should replace helper text when active.