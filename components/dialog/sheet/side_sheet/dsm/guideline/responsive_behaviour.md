### Horizontal responsive behaviour

The Side sheet width adapts to the viewport according to the selected Size variant and the responsive grid of each platform.  
The Side sheet is anchored to either the Start or End edge of the viewport, depending on its placement.

Because the Side sheet is attached to the edge of the viewport, its width is defined by a combination of the grid margin and the specified number of columns. For each breakpoint, the defined column span must therefore be combined with the corresponding grid margin. For example, at the md breakpoint (736–1023 px), the Side sheet uses 7 columns + 1 grid margin for the Default size, and 6 columns + 1 grid margin for the Small size. The grid margin is applied on the side opposite to the viewport edge where the Side sheet is anchored.

The Side sheet follows the defined column spans at smaller breakpoints and progressively reduces its relative width at larger breakpoints to preserve sufficient visibility of the underlying content. At larger breakpoints, a maximum width is applied to prevent the Side sheet from becoming disproportionately wide.

| Breakpoint | Viewport width | Default | Small |
|---|---|---|---|
| 2xs | 1–389 px | 12 columns | 11 columns |
| xs | 390–479 px | 12 columns | 11 columns |
| sm | 480–735 px | 10 columns | 9 columns |
| md | 736–1023 px | 7 columns | 6 columns |
| lg | 1024–1319 px | 5 columns (max-width:460) | 4 columns (max-width:420 \| min-width:380) |
| xl | 1320–1639 px | 4 columns (max-width:520) | 3 columns (max-width:480 \| min-width:420) |
| 2xl | 1640–1879 px | 4 columns (max-width:520) | 3 columns (max-width:480 \| min-width:420) |
| 3xl | 1880+ px | 3 columns (max-width:600) | 2 columns (max-width:520 \| min-width:440) |

### Vertical responsive behaviour

The Side sheet occupies the full available viewport height regardless of the selected Size variant or breakpoint.  
Unlike the Modal dialog, the Side sheet does not use different height specifications for its Default and Small sizes. Its height always spans the full available viewport, while the Size variant only affects its horizontal width and internal layout scale.  
When the Side sheet content exceeds the available viewport height, the content area becomes vertically scrollable while the Side sheet remains fixed to the viewport edge.