### Keyboard Support

1. **`Tab`** moves focus forward through each digit box in left-to-right order; **`Shift+Tab`** moves focus backward.
2. Typing a valid digit (0–9) automatically advances focus to the next empty box; typing in the last box keeps focus on that box.
3. **`Backspace`** deletes the current digit and moves focus to the previous box; pressing Backspace in an empty box moves to the previous box without deleting.
4. **`Enter`** submits the form when all required digits are filled; focus remains on the last box if submission fails.
5. Provide a visible focus indicator with outline/border ≥2px and contrast ≥3:1 around the active digit box.
6. Arrow keys (**`ArrowLeft`**, **`ArrowRight`**) may optionally navigate between boxes; document this behavior if implemented.