### Screen Reader Testing
- [ ] Test with NVDA (Windows), JAWS (Windows), VoiceOver (macOS/iOS), TalkBack (Android)
- [ ] Verify the accessible name, determinate value/percentage, and indeterminate "in progress" are announced without flooding

### Keyboard Testing
- [ ] Confirm the indicator is not a focus stop (non-interactive) yet does not trap focus, and the surrounding flow remains operable
- [ ] Verify any associated controls (cancel, retry) are reachable and focus is visible

### Motion & Zoom Testing
- [ ] With reduced-motion enabled, essential progress is still conveyed without animation
- [ ] At 200% zoom and reflow, the indicator stays visible, proportional, and unclipped

Resources: [Orange Accessibility Testing Guide](https://a11y-guidelines.orange.com/en/)