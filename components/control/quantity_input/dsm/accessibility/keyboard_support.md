## Keyboard Support

1. `Tab` moves focus to the quantity input field; `Shift+Tab` moves focus backward to the previous focusable element.
2. Arrow keys (`Up`/`Down`) increment or decrement the value by one unit when the input has focus.
3. `Enter` key submits the form if the input is part of a form, or triggers the associated action.
4. `Escape` key clears focus from the input field if no other action is defined.
5. Increment and decrement buttons must be keyboard-accessible and activated with `Enter` or `Space`.
6. Focus order follows left-to-right, top-to-bottom sequence: label → input field → increment/decrement buttons.
7. Provide a visible focus indicator with outline or border ≥2px and contrast ≥3:1 around the active element.
8. Ensure focus is not trapped within the component; users must be able to move focus forward and backward freely.