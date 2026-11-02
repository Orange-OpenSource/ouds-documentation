**`Filled`** Filled cards use a background surface to visually separate their content from the surrounding interface. By default, the card is displayed on a bg/primary background. To display the card on another supported background surface, designers should use the appropriate parent container rather than manually overriding the component's predefined visual properties. Unlike the Action card, the Card component is not interactive. Its background does not provide interaction feedback for the card itself. Any interactive elements within the slot retain their own independent interaction states.

**`Outlined`** Outlined cards define their boundaries with a border instead of a background fill. The container remains transparent, allowing the surrounding surface to show through.

**`Elevated`** Elevated cards create visual separation through a predefined shadow, giving the card a raised appearance. The background context is defined by the surrounding surface, while the card retains its own predefined elevation and visual support layers. The Card component remains non-interactive, regardless of its visual treatment.

&nbsp;

### Inverse background
Inverse backgrounds introduce a different color context within the interface. Text, icons, and interactive elements must adapt to the appropriate light or dark theme to maintain readability and contrast.

⚠️ Only the predefined stroke, divider, and background colors specified for this component may be used. Custom colors are not allowed.