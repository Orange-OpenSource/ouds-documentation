The Background Boolean property controls the visibility of the predefined color/action/support/enabled layer within the Card component. This property is available for the Filled and Elevated styles when State = Enabled.

**`True`** Displays the predefined color/action/support/enabled layer within the Card, over the underlying surface.

**`False`** Hides the internal Background layer, leaving the underlying surface visible without the additional support treatment.

&nbsp;

### ⚠️ Surface customization
In the Filled style, designers can place the Card inside an additional Surface frame to customize its base background using supported tokens, such as surface/primary, surface/secondary, or surface/tertiary etc...

This external frame acts as the underlying surface of the Card and is independent of the component's internal Background layer.  
The Background Boolean can be enabled or disabled independently of the selected Surface.

For other styles:  
• Elevated: Uses its predefined surface/primary background. The Background Boolean remains available, but the external Surface customization is not supported.  
• Outlined: Does not support the Background Boolean or additional Surface customization.

⚠️ The external Surface frame must use predefined OUDS surface tokens. The Card's internal Background layer must not be manually modified or replaced.

⚠️ When Rounded corner = True, the external Surface frame must use a predefined OUDS corner-radius token matching the Card's corner-radius value. This ensures consistent corner alignment between the Card and its underlying Surface.