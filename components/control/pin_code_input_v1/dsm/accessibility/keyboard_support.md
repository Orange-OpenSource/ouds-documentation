### Keyboard Support

1. `Tab` moves focus into the first empty digit box; `Shift+Tab` moves focus out to the previous form element.
2. Typing a valid numeric character (`0`–`9`) auto-advances focus to the next digit box (left→right); no auto-advance occurs on the last box.
3. `Backspace` clears the current digit and moves focus to the previous box; on the first box, Backspace clears the digit without moving focus.
4. `Arrow Left` / `Arrow Right` navigate between digit boxes without clearing content; wrap is not supported (focus stops at first/last box).
5. Provide a visible focus indicator with outline/border **≥2px** and contrast **≥3:1** against the background.