## Keyboard Support

1. `Tab` moves focus to the first empty digit box or the first box if all are empty.
2. `Shift+Tab` moves focus backward from the component to the previous focusable element.
3. Arrow keys (`Left`/`Right`) navigate between digit boxes without deleting content.
4. `Backspace` deletes the current digit and moves focus to the previous box.
5. `Delete` removes the current digit and keeps focus on the same box.
6. `Enter` submits the form when all required digits are filled.
7. Number keys (`0`-`9`) enter digits and automatically advance focus to the next box.
8. Provide a visible focus indicator: outline or border ≥2px with contrast ≥3:1 against the background.
9. Focus order moves left-to-right through digit boxes, then to submit button or next form element.
10. Pasted content auto-distributes across boxes without breaking focus management.