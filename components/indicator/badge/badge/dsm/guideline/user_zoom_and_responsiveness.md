**Max-width vs full-width**
This component have a max-width.
It is not possible to set this component to use the full available width (of the screen or the container).

**User zoom in/out**
- Componet must always scale proportionally with user zoom.
- In order to preserve the minimun interactive area during user zoom out, this component have:
  - Large size: a min-width and a min-height **of 20px**
  - Medium size: a min-width and a min-height **of 16px**
  - Small size: a min-width and a min-height **of 12px**
  - Xsmall size: a min-width and a min-height **of 8px**
- Even if, the component has a max-height or a max-width for resizing control purposes, technically, during user zoom in, these limitations are not fixed but must be scalable in order to adapt to the user's zoom level.
