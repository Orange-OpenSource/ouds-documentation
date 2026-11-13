Choose the component based on where the interaction happens, not on its visual style or the number of elements.  
A single action can belong either to a Card or to an Action card.

| Interaction pattern | Actions | Use | Interactive area |
|---|---|---|---|
| Display information only | 0 | Card | No interactive target |
| Provide one explicit CTA | 1 | Card | Only the internal button or link |
| Provide independent CTAs | 2+ | Card | Each internal control independently |
| Make the whole card one action | 1 | Action card | Available card surface |
| Reinforce the same action visually | 1 | Action card | One target; CTA is not focusable |
| Add one different secondary action | 2 | Action card | Primary region + secondary target |
| Add several secondary actions | 3+ | Action card | Primary region + independent targets |

Use Card when the container itself does nothing. Use Action card when the available card surface triggers a primary action.

Action card with independent secondary controls is conditional on platform and accessibility validation.  
If unsupported, use Card with an explicit primary CTA and separate secondary controls.  
Never nest links or buttons inside the primary card link/button; each independent action needs its own focus target
