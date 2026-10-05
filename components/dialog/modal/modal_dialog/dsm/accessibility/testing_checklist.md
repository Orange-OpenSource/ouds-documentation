### Screen Reader Testing

- [ ] Test with NVDA (Windows), JAWS (Windows), VoiceOver (macOS/iOS), TalkBack (Android)
- [ ] Verify the dialog role and title are announced on opening, the page behind is not reachable, and actions are read in the order Primary, Secondary, Tertiary

### Keyboard Testing

- [ ] Focus moves into the dialog on opening, Tab and Shift+Tab cycle inside it, Escape closes it, focus returns to the trigger
- [ ] Focus indicator visible (≥3:1 contrast) on every control and never hidden behind sticky actions

### Functional Testing

- [ ] Verify the opening and closing animation is removed when Reduced Motion is enabled, and that a static backdrop does not close the dialog on outside click

Resources: [Orange Accessibility Testing Guide](https://a11y-guidelines.orange.com/en/web/test/)