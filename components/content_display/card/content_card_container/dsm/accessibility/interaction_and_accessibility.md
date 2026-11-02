• The card itself does not receive Hover, Focus or Pressed states and must not behave as a button or link.

• Interactive elements placed within the slot, such as buttons and links, remain independently accessible and retain their own interaction states.

• Each interactive element must have an appropriate semantic role and a meaningful accessible name.

• Keyboard focus must be applied to the individual interactive elements, not to the card container itself.

• When the card is Disabled, nested interactive components must also be disabled and must not respond to user interaction.