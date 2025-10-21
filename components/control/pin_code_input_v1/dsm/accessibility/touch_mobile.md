### Touch & Mobile

1. Provide touch targets **≥48×48px** for each digit box with spacing **≥8px** between adjacent boxes.
2. Trigger numeric keyboard using `inputmode="numeric"` on each input element; ensure `type="text"` to allow paste and SMS autofill.
3. Support paste gesture via long-press context menu; distribute pasted digits across all boxes automatically (e.g., pasting "123456" fills all six boxes in sequence).
4. Support both portrait and landscape orientations; ensure digit boxes remain visible and accessible without horizontal scroll at 100% zoom.