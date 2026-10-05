### Screen Reader Testing

- [ ] Test with NVDA (Windows), JAWS (Windows), VoiceOver (macOS/iOS), TalkBack (Android)
- [ ] Verify the sheet role and title are announced on opening, the page behind is not reachable, and actions are read in the order Primary, Secondary, Tertiary

### Keyboard Testing

- [ ] Focus moves into the sheet on opening, Tab and Shift+Tab cycle inside it, Escape closes it, focus returns to the trigger
- [ ] Focus indicator visible (≥3:1 contrast) on every control and never hidden behind sticky actions

### Functional Testing

- [ ] Verify the slide animation is removed when Reduced Motion is enabled, that a static backdrop does not close the sheet on outside click, and that Start and End follow the reading direction in RTL

Resources: [Orange Accessibility Testing Guide](https://a11y-guidelines.orange.com/en/web/test/)