### Horizontal responsive behaviour

The modal width adapts to the viewport according to the selected Size variant and the responsive grid of each platform.  
The modal follows the defined column spans at larger breakpoints, while smaller viewport widths use fixed horizontal margins to preserve sufficient spacing from the viewport edges.

| Breakpoint | Viewport width | Default | Small |
|---|---|---|---|
| 2xs | 1–389 px | 16 px margin | 16 px margin |
| xs | 390–479 px | 16 px margin | 16 px margin |
| sm | 480–735 px | 10 columns | 10 columns |
| md | 736–1023 px | 10 columns | 8 columns |
| lg | 1024–1319 px | 10 columns | 6 columns |
| xl | 1320–1639 px | 8 columns | 4 columns |
| 2xl | 1640–1879 px | 8 columns | 4 columns |
| 3xl | 1880+ px | 8 columns | 4 columns |

For the 2xs and xs breakpoints, the modal does not follow a column-based grid and instead maintains a 16 px margin from the viewport edges.

&nbsp;

### Vertical responsive behaviour

The modal height adapts to the viewport according to the selected Size variant and the responsive breakpoint.  
The Default size uses a larger proportion of the available viewport, while the Small size remains more compact. When the modal content exceeds the available height, the content area becomes vertically scrollable.

| Breakpoint | Default | Small |
|---|---|---|
| 2xs | 16 px margin | 50% of viewport |
| xs | 16 px margin | 50% of viewport |
| sm | 90% of viewport | 50% of viewport |
| md | 90% of viewport | 50% of viewport |
| lg | 90% of viewport | 60% of viewport |
| xl | 90% of viewport | 60% of viewport |
| 2xl | 90% of viewport | 60% of viewport |
| 3xl | 90% of viewport | 50% of viewport |