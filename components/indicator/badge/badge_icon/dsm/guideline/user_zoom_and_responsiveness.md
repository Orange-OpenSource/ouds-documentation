**Max-width vs full-width**
This component have a max-width and a max-height.
It is not possible to set this component to use the full available width (of the screen or the container).

**User zoom in/out**
- Icons must always scale proportionally with user zoom. Icon resizing must never be blocked.
- In order to preserve the minimun interactive area during user zoom out, this component have:
  - Large size: a min-width and a min-height **of 20px**
  - Medium size: a min-width and a min-height **of 16px**
- Even if, the component has a max-height or a max-width for resizing control purposes, technically, during user zoom in, these limitations are not fixed but must be scalable in order to adapt to the user's zoom level.
